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

class Output:
    def __init__(self, addr, value, n, tx_index):
        self.n = n
        self.value = value
        self.address = addr
        self.tx_index = tx_index
class Input:
    def __init__(self, addr, value, n, tx_index):
        self.n = n
        self.value = value
        self.address = addr
        self.tx_index = tx_index
class Transaction:
    def __init__(self, t, block_height=None):
        self.block_height = block_height
        self.time = t['received_time']
        self.confirmation_mins = t['confirmation_mins']
        self.hash = t['hash']
        self.tx_index = t['tx_index']
        self.size = t['size']
        self.inputs = []
        self.outputs = []
        
        if self.block_height is None:
            self.block_height = -1

class Neo4j(object):

    # Returns transactions matching a block stored in the Neo4j db
    @staticmethod
    def get_block_data(block=411293):
        query = "MATCH (n:Block)-[:STORED_IN]-(transaction) WHERE n.height = " + str(block) + " RETURN transaction"
        result = graph.cypher.execute(query)
        txs = []
        for record in result.records:
            transaction = record.transaction
            tx = Transaction(transaction, block)
            # Inputs
            for rel in graph.match(end_node=transaction, rel_type=input_in):
                value = rel['value']
                tx_index = rel['tx_i']
                n = rel['tx_n']
                addr = rel.start_node["address"]
                print("Ao: " + str(addr) + " Value: " + str(value) + " Txi: " + str(tx_index) + ":" + str(n))
                tx.inputs.append(Input(addr, value, n, tx_index))
            # Outputs
            for rel in graph.match(end_node=transaction, rel_type=output_in):
                value = rel['value']
                tx_index = rel['tx_i']
                n = rel['tx_n']
                addr = rel.start_node["address"]
                print("Ai: " + str(addr) + " Value: " + str(value) + " Txi: " + str(tx_index) + ":" + str(n))
                tx.outputs.append(Output(addr, value, n, tx_index))

            txs.append(tx)

        return txs

    @staticmethod
    def get_tx_input_data(hash='9624905d95b0820c4a410f6265ea7bcb1cc8fa575c65210641f474e0a439243b'):
        query = "MATCH (tx:Transaction)-[:INPUT_IN]-(input) WHERE tx.hash = '" + str(hash) + "' RETURN input"
        result = graph.cypher.execute(query)
        return result

        # for record in result.records:
        #     input = record.input
        #      input = Input()



    @staticmethod
    def import_difficulty(start_block):
        end_block = start_block + 2016 + 1

        for i in range(start_block, end_block):
            print("Importing block: " + str(i) + " of " + str(end_block))
            Neo4j.import_block(i)

    @staticmethod
    def setup_db():
        graph.schema.create_uniqueness_constraint(addr_type, "address")
        graph.schema.create_uniqueness_constraint(tx_type, "hash")
        graph.schema.create_uniqueness_constraint(block_type, "height")

    @staticmethod
    def import_block(block_height):
        print("Neo4j: Getting Block " + str(block_height))
        blocks = blockexplorer.get_block_height(str(block_height), api_code="87575b65-eb36-4322-a0a1-43c2b705479f")
        block = blocks[0]

        print("Neo4j: Adding Block to DB")
        block_node = graph.merge_one(block_type, "height", block.height)
        block_node['time'] = block.time
        block_node['received_time'] = block.received_time
        block_node['n_tx'] = block.n_tx
        block_node['size'] = block.size
        block_node.push()

        transactions = Blockchain.process_transactions(block.transactions, block.received_time)
        print("Neo4j: Adding Txs to DB")
        for txi, tx in enumerate(transactions):
        
            tx_node = graph.merge_one(tx_type, "hash", tx.hash)
            tx_node['tx_index'] = tx.tx_index
            tx_node['size'] = tx.size
            tx_node['n_inputs'] = len(tx.inputs)
            tx_node['n_outputs'] = len(tx.outputs)
            tx_node['received_time'] = tx.time
            tx_node['confirmation_mins'] = tx.confirmation_mins
            tx_node['mempool_size'] = tx.mempool_size
            input_amnt = 0
            output_amnt = 0
        
            tx_stored_in_block = Relationship(tx_node, stored_in, block_node)
            graph.create(tx_stored_in_block)

            to_create = []
            for inp in tx.inputs:
                if hasattr(inp, 'address'):
                    address = inp.address
                    value = inp.value
                else:
                    address = 'c0'+ str(block.height)
                    era = (block_height/COINBASE_ERA_LENGTH) + 1
                    #print("Coinbase Era: " + str(era))
                    value = float(5000000000)/float(era)
                    
                inp_node = graph.merge_one(addr_type, 'address', address)

                # Previous tx index, unavailable for coinbase
                tx_i = 0
                tx_n = -1
                if hasattr(inp, 'tx_index'):
                    tx_i = inp.tx_index
                    tx_n = inp.n
                
                input_amnt += value
                node_input_in_tx = Relationship(inp_node, input_in, tx_node, value=value,
                                                tx_i=tx_i, tx_n=tx_n)
                to_create.append(node_input_in_tx)
        
            outputs = tx.outputs
            for out in outputs:
                address = out.address
                if not address:
                    address = "a" + str(tx.tx_index) + ":" + str(out.n)
                    #print("Tx hash: " + tx.hash)
                    #print("Addr: " + address)
                value = out.value
                tx_i = tx.tx_index
                tx_n = out.n
                out_node = graph.merge_one("Address",'address', address)
        
                output_amnt += value
                node_output_in_tx = Relationship(out_node, output_in, tx_node, value=value,
                                                 tx_i=tx_i, tx_n=tx_n)
                to_create.append(node_output_in_tx)

            fee = input_amnt - output_amnt
            tx_node['input_amount'] = input_amnt
            tx_node['output_amount'] = output_amnt
            tx_node['fee'] = fee
            tx_node['fee_per_byte'] = float(fee)/float(tx.size)
            tx_node.push()
            
            graph.create(*to_create)

            if txi % 500 == 0:
                print("---- Status: " + str(txi) + ":" + str(len(transactions)))

        print("Block " + str(block_height) + " done with " + str(len(transactions)) + " transactions.")

