import os
import pika
import uuid
import networkx as nx

# For base dir location to save files
from django.conf import settings

# For celery task processes
from backend.celery import app

# For API graphing request
from models import BlockVizRequest
# For transaction data
from blockchain_wrapper import Blockchain
# For visualtion
from graph import Graph

file_dir = settings.BASE_DIR + "/data/Connected/"

class GephiRpcClient(object):
	def __init__(self):
		self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
		self.channel = self.connection.channel()
		
		result = self.channel.queue_declare(exclusive=True)
		self.callback_queue = result.method.queue

		self.channel.basic_consume(self.on_response, no_ack=True, queue=self.callback_queue)

	def on_response(self, ch, method, props, body):
		if self.corr_id == props.correlation_id:
			self.response = body

	def call(self, n):
		self.response = None
		self.corr_id = str(uuid.uuid4())
		self.channel.basic_publish(exchange='',
								   routing_key='ToLayout',
								   properties=pika.BasicProperties(
								   	reply_to = self.callback_queue,
								   	correlation_id = self.corr_id,),
								   body=str(n))
		while self.response is None:
			self.connection.process_data_events()
		return self.response


@app.task(bind=True)
def generate_block_viz(self, id):
	query = BlockVizRequest.objects.get(pk=id)

	# Block data parameters
	start = query.start
	end = query.end
	# For subcomponents
	threshold = query.threshold

	txs = Blockchain.get_transactions_by_block(start, end)

	G = Graph.get_transaction_graph(txs)
	graph_path = file_dir + str(id) + ".graphml"
	nx.write_graphml(G, graph_path)
	print("Sent:" + graph_path)

	gephi_rpc = GephiRpcClient()
	response = gephi_rpc.call(graph_path)
	print("Response: " + response)