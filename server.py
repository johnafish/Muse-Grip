import argparse
import threading

from pythonosc import dispatcher
from pythonosc import osc_server


def blinkHandler(*data):
	print(data)

# Thanks osc_server on github for this code
global dispatcher, Dispatcher, server
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="localhost", help="The ip to listen on")
parser.add_argument("--port",type=int, default=1337, help="The port to listen on")
args = parser.parse_args()
dispatcher = dispatcher.Dispatcher()
dispatcher.map("/muse/elements/blink", blinkHandler)
server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
server_thread = threading.Thread(target=server.serve_forever)
server_thread.start()