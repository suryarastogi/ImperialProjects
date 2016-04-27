import os
import pika
import uuid
import networkx as nx

# General Utility functions
from utils import Utils

# For base dir location to save files
from django.conf import settings

# For celery task processes
from backend.celery import app

# For API graphing request
from models import BlockVizRequest
# For graph sub components
from models import Subcomponent
# For transaction data
from blockchain_wrapper import Blockchain
# For visualtion
from graph import Graph

connected_dir = settings.BASE_DIR + "/data/Connected/"
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

@app.task(bind=True)
def generate_block_viz(self, id):
    query = BlockVizRequest.objects.get(pk=id)

    if not query.completed:
        # Block data parameters
        start = query.start
        end = query.end
        # For subcomponents
        threshold = query.threshold

        txs = Blockchain.get_transactions_by_block(start, end)

        G = Graph.get_transaction_graph(txs)
        cgraph_path = connected_dir + str(id) + ".graphml"
        nx.write_graphml(G, cgraph_path)

        print("Queing subcomponents")
        generate_subcomponents.delay(id)

        print("Sending:" + cgraph_path)
        gephi_rpc = GephiRpcClient()
        response = gephi_rpc.call(cgraph_path)
        print("Response: " + response)

        G = nx.read_graphml(response)
        G = Graph.colour_transaction_graph(G)

        graph_path = coloured_dir + str(id) + ".graphml"
        nx.write_graphml(G, graph_path)

        print("Renaming Attributes")
        Utils.fix_graphml(graph_path)

        query.completed = True
        query.path = graph_path
        query.save()
        # Remove the temporary layout file
        os.remove(response)
        # Remove the temporary connection file
        os.remove(cgraph_path)

@app.task(bind=True)
def generate_subcomponents(self, id):
    query = BlockVizRequest.objects.get(pk=id)

    if query.completed:
        graph_path = coloured_dir + str(id) + ".graphml"
    else:
        graph_path = connected_dir + str(id) + ".graphml"

    G = nx.read_graphml(graph_path)
    
    num_subcomps = nx.number_connected_components(G)
    i = 0
    for g in nx.connected_component_subgraphs(G):
        if len(g.nodes()) > query.threshold:
            graph_name = str(id) + "C" + str(i) + ".graphml"
            graph_path = connected_dir + graph_name
            nx.write_graphml(g, graph_path)
            generate_subcomponent.delay(id=id, path=graph_path)
            
        i += 1

@app.task(bind=True)
def generate_subcomponent(self, id, path):
    query = BlockVizRequest.objects.get(pk=id)
    sc = Subcomponent.objects.create(request=query)

    print("Sending:" + path)
    gephi_rpc = GephiRpcClient()
    response = gephi_rpc.call(path)
    print("Response: " + response)

    # Remove the temporary connection file
    os.remove(path)

    G = nx.read_graphml(response)

    # Remove the temporary layout file
    os.remove(response)

    G = Graph.colour_transaction_graph(G)

    graph_name = str(id) + "C" + str(sc.pk) + ".graphml"
    graph_path = coloured_dir + graph_name
    
    nx.write_graphml(G, graph_path)

    print("Renaming Attributes")
    Utils.fix_graphml(graph_path)

    sc.path = graph_path
    sc.save()