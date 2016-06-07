# To Produce graphs based on Neo4j data

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import networkx as nx

from API.neo4j import Neo4j
from models import BlockVizRequest
from utils import Utils

class Graphing(object):

    @staticmethod
    def get_block_viz_txs(id):
        query = BlockVizRequest.objects.get(pk=id)
        txs = []
        if query.completed:
            path = query.path
            G = nx.read_graphml(path)
            nodes = G.nodes()
            for node in nodes:
                if G.node[node]['type'] == 'tx':
                    # Empty object
                    tx = type('Transaction', (object,), {})()
                    tx.confirmation_mins = G.node[node]['confirmation_mins']
                    tx.mempool_size = G.node[node]['mempool_size']
                    tx.fee_per_byte = G.node[node]['fee_per_byte']
                    txs.append(tx)
        return txs


    @staticmethod
    def graph_block_request(id):
        txs = Graphing.get_block_viz_txs(id)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        X = [tx.fee_per_byte for tx in txs]
        Y = [float(tx.mempool_size)/float(1024*1024) for tx in txs]
        Z = [tx.confirmation_mins for tx in txs]
        ax.scatter(X,Y,Z)

        ax.set_xlabel('Fee per byte (satoshi/byte)')
        ax.set_ylabel('Mempool Size (MB)')
        ax.set_zlabel('Confirmation Time (mins)')
        plt.show()

    @staticmethod
    def graph_address_request():
        pass


    @staticmethod
    def graph_block(block):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        txs = Neo4j.get_txs_in_block(block)
        X = [tx.fee_per_byte for tx in txs]
        Y = [tx.mempool_size for tx in txs]
        Z = [tx.confirmation_mins for tx in txs]
        ax.scatter(X,Y,Z)

        ax.set_xlabel('Fee per byte (satoshi/byte)')
        ax.set_ylabel('Mempool Size (bytes)')
        ax.set_zlabel('Confirmation Time (mins)')
        plt.show()
