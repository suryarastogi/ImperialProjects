import urllib2
import json
from utils import Utils
from blockchain import blockexplorer
from collections import deque

# Class to manage blockchain(.info) data
# API Doc
# https://github.com/blockchain/api-v1-client-python/blob/master/docs/blockexplorer.md

#Using classes from API client
class Input:
    def __init__(self, i):
        obj = i.get('prev_out')
        if obj is not None:
            # regular TX
            self.n = obj['n']
            self.value = obj['value']
            self.address = obj['addr']
            self.tx_index = obj['tx_index']
            self.type = obj['type']
            self.script = obj['script']
            self.script_sig = i['script']
            self.sequence = i['sequence']
        else:
            # coinbase TX
            self.script_sig = i['script']
            self.sequence = i['sequence']


class Output:
    def __init__(self, o):
        self.n = o['n']
        self.value = o['value']
        self.address = o.get('addr')
        self.tx_index = o['tx_index']
        self.script = o['script']
        self.spent = o['spent']

class Transaction:
    def __init__(self, t):
        self.double_spend = t.get('double_spend', False)
        self.block_height = t.get('block_height')
        self.time = t['time']
        self.relayed_by = t['relayed_by']
        self.hash = t['hash']
        self.tx_index = t['tx_index']
        self.version = t['ver']
        self.size = t['size']
        self.inputs = [Input(i) for i in t['inputs']]
        self.outputs = [Output(o) for o in t['out']]
        
        if self.block_height is None:
            self.block_height = -1

api_key = "87575b65-eb36-4322-a0a1-43c2b705479f"
class Blockchain(object):
    # "?api_code=" + api_key
    @staticmethod
    def get_tx(index):
        return blockexplorer.get_tx(index, api_code=api_key)

    @staticmethod
    def trace_transaction_complete(index):
        txs = []

        q = deque()
        q.append(index)

        while len(q) > 0:
            print("Q: " + str(len(q)) + " txs:" + str(len(txs)))
            tx = Blockchain.get_tx(q.popleft())
            txs.append(tx)

            inputs = tx.inputs
            for inp in inputs:
                # Else coinbase
                if hasattr(inp, 'address'):
                    q.append(str(inp.tx_index))
        return txs

    @staticmethod
    def trace_transaction(index, limit=50):
        txs = []

        q = deque()
        q.append(index)

        i = 0
        while len(q) > 0 and i < limit:
            print("Q: " + str(len(q)) + " i:" + str(i) + " txs:" + str(len(txs)))
            tx = Blockchain.get_tx(q.popleft())
            txs.append(tx)

            inputs = tx.inputs
            for inp in inputs:
                # Else coinbase
                if hasattr(inp, 'address'):
                    q.append(str(inp.tx_index))
            i = i + 1
        return txs

    @staticmethod
    def get_block_json(block):
        #https://blockchain.info/block-index/$block_index?format=json
        url = "https://blockchain.info/rawblock/" + str(block) + "?format=json" + "&api_code=" + api_key
        #print(url)
        jso = urllib2.urlopen(url)
        block = json.load(jso)
        return block

    # Client provided by blockchain does not return more than 50 most recent txs
    @staticmethod
    def get_transactions_by_addr(addr, limit=50):
        #addr = "1dice8EMZmqKvrGE4Qc9bUFf9PX3xaYDp"
        limit_reached = False
        base_url = "https://blockchain.info/address/" + addr + "?format=json" + "&api_code=" + api_key
        stop = False
        txs = []
        while len(txs) < limit and not stop:
            print(str(len(txs)) + ":" + str(limit))
            url = base_url + "&offset=" + str(len(txs))
            jso = urllib2.urlopen(url)
            addr_obj = json.load(jso)
            new_txs = [Transaction(tx) for tx in addr_obj['txs']]
            txs += new_txs
            if len(new_txs) < 50:
                stop = True

        return txs

    @staticmethod
    def get_transactions_by_block_json(start, end):
        transactions = []
        for i in range (start, end):
            print(i)
            block = BlockchainUtils.get_block_json(i) #blockexplorer.get_block_height(str(i), api_code=api_key)
            #block = blocks[0]
            transactions += block["tx"] #block.tx_indexes

        return transactions #transactions[0]["out"] or transactions[0]["inputs"]

    # Returns all transactions from the start block to end block

    @staticmethod
    def process_transactions(txs, block_time):
        for tx in txs:
            tx.confirmation_mins = Utils.get_mins_between(tx.time, block_time)
        return txs


    @staticmethod
    def get_transactions_by_block(start, end):
        transactions = []
        for i in range (start, end):
            print(i)
            blocks = blockexplorer.get_block_height(str(i), api_code=api_key)
            block = blocks[0]
            transactions += Blockchain.process_transactions(block.transactions, block.received_time)


        return transactions