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
# For API graphing request and graph subcomponent
from models import BlockVizRequest, Subcomponent
# For Address graph
from models import AddressVizRequest
# For Trace Tx Visualisation
from models import TraceTxVizRequest
# For transaction data
from blockchain_wrapper import Blockchain
# For visualtion
from graph import Graph

data_dir = settings.BASE_DIR + "/data"
connected_dir = data_dir + "/Connected/"
coloured_dir = data_dir + "/Coloured/"

# Remote procedure call for Gephi Layout Task
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
def generate_trace_tx_viz(self,id):
    query = TraceTxVizRequest.objects.get(pk=id)
    if not query.completed:
        tx_index = query.hash_index

        txs = Blockchain.trace_transaction(tx_index, 1000)
        #G = Graph.get_transaction_graph(txs)
        G = Graph.get_trace_graph(txs)

        cgraph_path = connected_dir + Utils.get_trace_tx_viz_file_name(id)
        nx.write_graphml(G, cgraph_path)
        Utils.fix_xml(cgraph_path)

        print("Sending:" + cgraph_path)
        gephi_rpc = GephiRpcClient()
        response = gephi_rpc.call(cgraph_path)
        print("Response: " + response)

        G = nx.read_graphml(response)
        G = Graph.colour_trace(G)

        graph_path = coloured_dir + Utils.get_trace_tx_viz_file_name(id)
        nx.write_graphml(G, graph_path)

        print("Renaming Attributes")
        Utils.fix_xml(graph_path)

        query.completed = True
        query.path = graph_path
        query.save()
        # Remove the temporary layout file
        os.remove(response)
        # Remove the temporary connection file
        os.remove(cgraph_path)
    pass

@app.task(bind=True)
def generate_address_viz(self, id):
    query = AddressVizRequest.objects.get(pk=id)
    if not query.completed:
        address = query.address
        limit = query.tx_limit

        txs = Blockchain.get_transactions_by_addr(address, limit)
        G = Graph.get_transaction_graph(txs, address)

        cgraph_path = connected_dir + Utils.get_address_viz_file_name(id)
        nx.write_graphml(G, cgraph_path)
        Utils.fix_xml(cgraph_path)

        print("Sending:" + cgraph_path)
        gephi_rpc = GephiRpcClient()
        response = gephi_rpc.call(cgraph_path)
        print("Response: " + response)

        G = nx.read_graphml(response)
        G = Graph.colour_transaction_graph(G, address)

        graph_path = coloured_dir + Utils.get_address_viz_file_name(id)
        nx.write_graphml(G, graph_path)

        print("Renaming Attributes")
        Utils.fix_xml(graph_path)

        query.completed = True
        query.path = graph_path
        query.save()
        # Remove the temporary layout file
        os.remove(response)
        # Remove the temporary connection file
        os.remove(cgraph_path)

@app.task(bind=True)
def generate_block_viz(self, id):
    query = BlockVizRequest.objects.get(pk=id)

    if not query.completed:
        # Block data parameters
        start = query.start
        end = query.end
        # For subcomponents
        threshold = query.threshold

        # Get transactions and create graph
        txs = Blockchain.get_transactions_by_block(start, end)
        G = Graph.get_transaction_graph(txs)

        cgraph_path = connected_dir + Utils.get_block_viz_file_name(id)
        nx.write_graphml(G, cgraph_path)
        Utils.fix_xml(cgraph_path)

        print("Queing subcomponents")
        generate_subcomponents.delay(id)

        print("Sending:" + cgraph_path)
        gephi_rpc = GephiRpcClient()
        response = gephi_rpc.call(cgraph_path)
        print("Response: " + response)

        G = nx.read_graphml(response)
        G = Graph.colour_transaction_graph(G)

        graph_path = coloured_dir + Utils.get_block_viz_file_name(id)
        nx.write_graphml(G, graph_path)

        print("Renaming Attributes")
        Utils.fix_xml(graph_path)

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
        graph_path = coloured_dir + Utils.get_block_viz_file_name(id)
    else:
        graph_path = connected_dir + Utils.get_block_viz_file_name(id)

    G = nx.read_graphml(graph_path)
    num_subcomps = nx.number_connected_components(G)
    i = 0
    for g in nx.connected_component_subgraphs(G):
        if len(g.nodes()) > query.threshold and query.threshold > 0:
            graph_name = Utils.get_block_viz_sub_file_name(id, i)
            graph_path = connected_dir + graph_name
            nx.write_graphml(g, graph_path)
            Utils.fix_xml(graph_path)

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
    txs, txs_length = Graph.get_tx_indexes(G)

    # Remove the temporary layout file
    os.remove(response)

    G = Graph.colour_transaction_graph(G)

    graph_name = Utils.get_block_viz_sub_file_name(id, sc.pk)
    graph_path = coloured_dir + graph_name
    nx.write_graphml(G, graph_path)
    Utils.fix_xml(graph_path)

    sc.path = graph_path
    sc.txs = txs
    sc.txs_length = txs_length
    sc.save()