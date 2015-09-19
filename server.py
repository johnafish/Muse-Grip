import argparse

from pythonosc import dispatcher
from pythonosc import osc_server


# Thanks osc_server on github for this code
global dispatcher, Dispatcher, server
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="localhost", help="The ip to listen on")
parser.add_argument("--port",type=int, default=1337, help="The port to listen on")
args = parser.parse_args()