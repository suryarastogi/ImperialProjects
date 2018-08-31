from blockchain import blockexplorer

def getTransactions(height=364133, radius=0, debug=False):
    start = height - radius
    end = (height - radius) + 1
    
    transactions = []
    for i in range (start, end):
        blocks = blockexplorer.get_block_height(str(i))
        block = blocks[0]
        transactions += block.transactions #block.tx_indexes
    
    print_log("No. of Transactions" + str(len(transactions)), debug)
    return transactions

def print_log(msg, debug):
    if debug:
        print(msg)
    else:
        pass