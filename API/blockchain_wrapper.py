import urllib2
import json
from blockchain import blockexplorer
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
        txs_length = 0
        txs = []
        while len(txs) < limit:
            url = base_url + "&offset=" + str(len(txs))
            jso = urllib2.urlopen(url)
            addr_obj = json.load(jso)
            txs += [Transaction(tx) for tx in addr_obj['txs']]
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
    def get_transactions_by_block(start, end):
        transactions = []
        for i in range (start, end):
            print(i)
            blocks = blockexplorer.get_block_height(str(i), api_code=api_key)
            block = blocks[0]
            transactions += block.transactions

        return transactions