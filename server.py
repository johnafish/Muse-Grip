import argparse
import threading
import time
import serial
import configparser

from pythonosc import dispatcher
from pythonosc import osc_server


parser = configparser.ConfigParser()
parser.read("config.ini")
userValues = parser["USER_VALUES"]

desiredClenches = int(userValues["clenches"])
threshold = float(userValues["bound"])

legalValues = []
lastClenchPeriod = 0
ser = serial.Serial("COM6", 9600)

def numClenches(binaryTimestampedArray):
	secondlast = 0
	last = 0
	secondlast=0
	number = 0
	for node in binaryTimestampedArray:
		if node[0]==1 and last == 0 and secondlast == 0:
			number += 1;
		last=secondlast
		secondlast=node[0]
	return(number)

def clenchHandler(*data):
	global legalValues, lastClenchPeriod
	handleType, value = data
	print(value)
	curTime = time.time()
	legalValues.append([value, curTime])
	for node in legalValues:
		if node[1]<curTime-threshold:
			legalValues.pop(legalValues.index(node))
	numClenchPeriod = numClenches(legalValues)
	if numClenchPeriod==desiredClenches and lastClenchPeriod!=desiredClenches:
		ser.write(bytes([1]))
		print("serial print")
	
	lastClenchPeriod=numClenchPeriod

global dispatcher, Dispatcher, server
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="localhost", help="The ip to listen on")
parser.add_argument("--port",type=int, default=1337, help="The port to listen on")
args = parser.parse_args()
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/muse/elements/jaw_clench", clenchHandler)
server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()
 
#muse-io --osc osc.udp://localhost:1337 