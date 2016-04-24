#import blockchain
# Class to manage blockchain(.info) data
# API Doc
# https://github.com/blockchain/api-v1-client-python/blob/master/docs/blockexplorer.md


class BlockchainUtils(object):
    api_key = "87575b65-eb36-4322-a0a1-43c2b705479f"

	# Returns all transactions from the start block to end block
    @staticmethod
    def get_transactions_by_block(start=364133, end=364134):
	    transactions = []
	    for i in range (start, end):
	    	print(i)
	        #blocks = blockchain.blockexplorer.get_block_height(str(i), api_code=api_key)
	        #block = blocks[0]
	        #transactions += block.transactions #block.tx_indexes

	    return transactions