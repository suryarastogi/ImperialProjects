import os
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

file_dir = settings.BASE_DIR + "/data/"

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
	print(graph_path)