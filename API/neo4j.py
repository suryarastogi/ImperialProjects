# Neo4j Library
from py2neo import authenticate, Graph, Node, Relationship
from blockchain import blockexplorer
from blockchain_wrapper import Blockchain
COINBASE_ERA_LENGTH = 210000

graph = Graph("http://neo4j:admin@localhost:7474/db/data/")
addr_type = "Address" # address
tx_type = "Transaction" # (hash, tx_index, size, n_inputs, n_outputs, received_time, confirmation_mins)
block_type = "Block" # (height, time, received_time, n_tx, size)
input_in = "INPUT_IN"
output_in = "OUTPUT_IN"
stored_in = "STORED_IN"

class Neo4j(object):

    @staticmethod
    def setup_db():
        graph.schema.create_uniqueness_constraint(addr_type, "address")
        graph.schema.create_uniqueness_constraint(tx_type, "hash")
        graph.schema.create_uniqueness_constraint(block_type, "height")

    @staticmethod
    def import_block(block_height):
        blocks = blockexplorer.get_block_height(str(block_height), api_code="87575b65-eb36-4322-a0a1-43c2b705479f")
        block = blocks[0]

        block_node = graph.merge_one(block_type, "height", block.height)
        block_node['time'] = block.time
        block_node['received_time'] = block.received_time
        block_node['n_tx'] = block.n_tx
        block_node['size'] = block.size
        block_node.push()

        transactions = Blockchain.process_transactions(block.transactions, block.received_time)

        for txi, tx in enumerate(transactions):
        
            tx_node = graph.merge_one(tx_type, "hash", tx.hash)
            tx_node['tx_index'] = tx.tx_index
            tx_node['size'] = tx.size
            tx_node['n_inputs'] = len(tx.inputs)
            tx_node['n_outputs'] = len(tx.outputs)
            tx_node['received_time'] = tx.time
            tx_node['confirmation_mins'] = tx.confirmation_mins
            tx_node['mempool_size'] = tx.mempool_size
            tx_node.push()
        
            tx_stored_in_block = Relationship(tx_node, stored_in, block_node)
            graph.create(tx_stored_in_block)

            for inp in tx.inputs:   
                if hasattr(inp, 'address'):
                    address = inp.address
                    value = inp.value
                else:
                    address = '0'+ str(block.height)
                    era = (block_height/COINBASE_ERA_LENGTH) + 1
                    #print("Coinbase Era: " + str(era))
                    value = float(5000000000)/float(era)
                    
                inp_node = graph.merge_one(addr_type, 'address', address)
            
                node_input_in_tx = Relationship(inp_node, input_in, tx_node, value=value)
                graph.create(node_input_in_tx)
        
            outputs = tx.outputs
            for out in outputs:
                address = out.address
                if not address:
                    address = "a" + str(tx.tx_index) + ":" + str(out.n)
                    print("Tx hash: " + tx.hash)
                    print("Addr: " + address)
                value = out.value
        
                out_node = graph.merge_one("Address",'address', address)
        
                node_output_in_tx = Relationship(out_node, output_in, tx_node, value=value)
                graph.create(node_output_in_tx)

            #print(str(txi) + ":" + str(len(transactions)))
        print("Block " + str(block_height) + " done with " + str(len(transactions)) + " transactions.")

