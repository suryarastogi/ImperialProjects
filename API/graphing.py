# To Produce graphs based on Neo4j data

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import mpld3
import seaborn as sns

import networkx as nx

from API.neo4j import Neo4j
from models import BlockVizRequest, AddressVizRequest
from utils import Utils

class Graphing(object):

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
    def d3_fee_graph_block_request(id):
        query = BlockVizRequest.objects.get(pk=id)
        start = query.start
        end = query.end
        if end - start > 1:
            title = "Blocks [" + str(start) + ", " + str(end) + ")"
        else:
            title = "Block " + str(start)

        txs = Graphing.get_block_viz_txs(id)
        X = [tx.fee_per_byte for tx in txs]
        Y = [tx.confirmation_mins for tx in txs]

        fig, ax = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'))
        N = 100

        scatter = ax.scatter(X, Y)
        ax.grid(color='white', linestyle='solid')

        ax.set_title(title, size=20)
        ax.set_ylabel('Confirmation Time (mins)')
        ax.set_xlabel('Fee per byte (satoshi/byte)')

        labels = [tx.hash for tx in txs]
        tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
        mpld3.plugins.connect(fig, tooltip)

        mpld3.show()

    @staticmethod
    def d3_mempool_graph_block_request(id):
        query = BlockVizRequest.objects.get(pk=id)
        start = query.start
        end = query.end
        if end - start > 1:
            title = "Blocks [" + str(start) + ", " + str(end) + ")"
        else:
            title = "Block " + str(start)

        txs = Graphing.get_block_viz_txs(id)
        X = [float(tx.mempool_size)/float(1024*1024) for tx in txs]
        Y = [tx.confirmation_mins for tx in txs]

        fig, ax = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'))
        N = 100

        scatter = ax.scatter(X, Y)
        ax.grid(color='white', linestyle='solid')

        ax.set_title(title, size=20)
        ax.set_ylabel('Confirmation Time (mins)')
        ax.set_xlabel('Mempool Size (MB)')

        labels = [tx.hash for tx in txs]
        tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
        mpld3.plugins.connect(fig, tooltip)

        mpld3.show()

    @staticmethod
    def graph_address_request(id):
        query = AddressVizRequest.objects.get(pk=id)
        address = query.address
        offset = query.tx_offset
        limit = query.tx_limit

        title = address + " Transactions " + str(offset) + " to " + str(offset + limit)
        txs = Graphing.get_address_viz_txs(id)
        
        block_count = {}
        for tx in txs:

            if str(tx.block) in block_count:
                block_count[str(tx.block)] += 1
            else:
                block_count[str(tx.block)] = 1

        count = []
        key = []

        for block in sorted(block_count):
            count.append(block_count[block])
            key.append(block)

        ind = np.arange(0, len(block_count) * 2, 2)
        #ind = np.arange(len(block_count))  # the x locations for the groups
        width = 0.8       # the width of the bars
        fig, ax = plt.subplots()
        ax.xaxis.set_tick_params(pad=15)

        boxes = ax.bar(ind, count, width, color='b')

        ax.set_title(title, size=15)
        ax.set_ylabel('Transaction Count')
        ax.set_xlabel('Block')

        plt.xticks(ind, tuple(key), rotation='vertical')
        plt.subplots_adjust(bottom=0.15)
        plt.show()

    @staticmethod
    def d3_address_request(id):
        query = AddressVizRequest.objects.get(pk=id)
        address = query.address
        offset = query.tx_offset
        limit = query.tx_limit

        title = address + " Transactions " + str(offset) + " to " + str(offset + limit)
        txs = Graphing.get_address_viz_txs(id)
        
        block_count = {}
        for tx in txs:

            if str(tx.block) in block_count:
                block_count[str(tx.block)] += 1
            else:
                block_count[str(tx.block)] = 1

        count = []
        key = []

        for block in sorted(block_count):
            count.append(block_count[block])
            key.append(block)

        ind = np.arange(len(block_count))  # the x locations for the groups

        width = 0.8       # the width of the bars
        fig, ax = plt.subplots()
        ax.xaxis.set_tick_params(pad=15)

        boxes = ax.bar(ind, count, width, color='b')

        ax.set_title(title, size=20)
        ax.set_ylabel('Transaction Count')
        ax.set_xlabel('Block')

        for i, box in enumerate(boxes.get_children()):
            tooltip = mpld3.plugins.LineLabelTooltip(box, label=key[i])
            mpld3.plugins.connect(fig, tooltip)

        mpld3.plugins.connect(fig, tooltip)
        mpld3.show()

    @staticmethod
    def get_address_viz_txs(id):
        query = AddressVizRequest.objects.get(pk=id)
        txs = []
        if query.completed:
            path = query.path
            G = nx.read_graphml(path)
            nodes = G.nodes()
            for node in nodes:
                if G.node[node]['type'] == 'tx':
                    # Empty object
                    tx = type('Transaction', (object,), {})()
                    tx.block = G.node[node]['block']
                    txs.append(tx)
        return txs

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
                    tx.hash = G.node[node]['tx_hash']
                    tx.confirmation_mins = G.node[node]['confirmation_mins']
                    tx.mempool_size = G.node[node]['mempool_size']
                    tx.fee_per_byte = G.node[node]['fee_per_byte']
                    txs.append(tx)
        return txs

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
