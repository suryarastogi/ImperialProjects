'''
    Wires components together, and starts running the handler processsing jobs
'''
import sys
import json

from RabbitPuller import RabbitPuller
from GPRequester import GPRequester
from PredictionHandler import PredictionHandler

# First argument is type of configuration
if(len(sys.argv) > 1):
    option = sys.argv[1]
else:
    option = "test"

# Load configuration options
config_file = open('config.json')                       
config = json.load(config_file)

print("Attempting to load configuration option: %s" % option)
print("Using RabbitMQ server on: %s" % str(config[option]["host"]))
print("Accessing queue with username: %s" % str(config[option]["username"]))
print("Using password: %s" % str(config[option]["password"]))

prediction_queue_name = str(config["queue_names"]["pred"])
gp_queue_name = str(config["queue_names"]["gp"])

username = str(config[option]["username"])
password = str(config[option]["password"])
host = str(config[option]["host"])

gpr = GPRequester(username, password, host, gp_queue_name)
ph = PredictionHandler(gpr)
p = RabbitPuller(username, password, host, prediction_queue_name, ph.handle_request)

print("Awaiting Prediction Requests...")
p.start()