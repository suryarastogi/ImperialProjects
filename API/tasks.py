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
coloured_dir = settings.BASE_DIR + "/data/Coloured/"

# Remote procedure call for gephi layout task
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

def node_type(node):
    if node[0] == 'i':
        return 'input'
    elif node[0] == 'o':
        return 'output'
    elif node[0] == 't':
        return 'tx'
    else:
        return 'coinbase'

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

    G = nx.read_graphml(response)

    nodes = G.nodes()
    for node in nodes:
        colour = None

        if node_type(node) == 'input':
            # Orange
            G.node[node]['r'] = 255
            G.node[node]['g'] = 200
            G.node[node]['b'] = 0
        elif node_type(node) == 'output':
            # Blue
            G.node[node]['r'] = 0
            G.node[node]['g'] = 0
            G.node[node]['b'] = 255
        elif node_type(node) == 'tx':
            G.node[node]['r'] = 255
            G.node[node]['g'] = 255
            G.node[node]['b'] = 255
        else:
            G.node[node]['r'] = 0
            G.node[node]['g'] = 255
            G.node[node]['b'] = 0

    edges = G.edges_iter()
    for u, v in edges:
        colour = None
    
        if node_type(u) == 'tx':
            if node_type(v) == 'input':
                colour = 'orange'
            else:
                colour = 'blue'    
        elif node_type(v) == 'tx':
            if node_type(u) == 'input':
                colour = 'orange'
            else:
                colour = 'blue'
        else:
            colour = 'grey'
        
        if colour == 'grey':
            #Grey
            G[u][v]['r'] = 137
            G[u][v]['g'] = 137
            G[u][v]['b'] = 137
        elif colour == 'orange':
            #Orange
            G[u][v]['r'] = 255
            G[u][v]['g'] = 200
            G[u][v]['b'] = 0
        else:
            #Orange
            G[u][v]['r'] = 0
            G[u][v]['g'] = 0
            G[u][v]['b'] = 255

    graph_path = coloured_dir + str(id) + ".graphml"
    nx.write_graphml(G, graph_path)

    print("Renaming Attributes")
    replacements = {'d10':'g', 'd11':'weight', 'd0':'size', 'd1':'b', 'd2':'g', 'd3':'y', 'd4':'x', 'd5':'r', 
                    'd6':'label', 'd7':'edgeid', 'd8':'r', 'd9':'b'}
    lines = []
    with open(graph_path) as infile:
        #For strict ordering
        replace = ['d10', 'd11', 'd0', 'd1', 'd2','d3', 'd4', 'd5', 'd6', 'd7','d8', 'd9']
        for line in infile:
            for src in replace:
                line = line.replace(src, replacements[src])
            lines.append(line)
    with open(graph_path, 'w') as outfile:
        for line in lines:
            outfile.write(line)
