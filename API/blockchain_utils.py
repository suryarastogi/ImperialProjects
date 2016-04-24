import urllib2
import json
# Class to manage blockchain(.info) data
# API Doc
# https://github.com/blockchain/api-v1-client-python/blob/master/docs/blockexplorer.md


api_key = "87575b65-eb36-4322-a0a1-43c2b705479f"
class BlockchainUtils(object):
    # "?api_code=" + api_key
    @staticmethod
    def get_block_json(block):
        #https://blockchain.info/block-index/$block_index?format=json
        url = "https://blockchain.info/rawblock/" + str(block) + "?format=json" + "&api_code=" + api_key
        #print(url)
        jso = urllib2.urlopen(url)
        block = json.load(jso)
        return block

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
            #block = blocks[0]
            transactions = block.transactions

        return transactions