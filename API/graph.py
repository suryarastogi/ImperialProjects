import math
import networkx as nx

# Constants for Transaction graph generation
edge_scale = 5
addr_weight = 30
tx_out_weight = 1*edge_scale
tx_in_weight = 4*edge_scale 
scaling_constant = 26.00/10.00 # #Average from test block
COINBASE_ERA_LENGTH = 210000

class Graph(object):

#    Transaction Graph Generation Function
#    Takes list of Transactions (see [kaiko/blockchain]_wrapper file for details)
#    and an address to trace/highlight (as a string)

    @staticmethod
    def get_transaction_graph(transactions, highlight=None):
        G = nx.Graph()

        addrHistory = {}
        size_list = []
        base_block = None
        for i, tx in enumerate(transactions):
            #if i % 500 == 0:
            #    print(str(i) + ":" + str(len(transactions)))
            if base_block is None:
                base_block = tx.block_height

            gravity_x = float(tx.block_height) - float(base_block) 
            tx_id = "tx" + str(tx.hash)
            if hasattr(tx, 'confirmation_mins'): # and hasattr(tx, 'fee_per_byte'):
                # Has been processed with additional data
                if hasattr(tx, 'mempool_size'):
                    tx_node = G.add_node(tx_id, block=tx.block_height, tx_hash=tx.hash,
                                     gravity_x=gravity_x, confirmation_mins=tx.confirmation_mins,
                                     type='tx', fee_per_byte=tx.fee_per_byte, 
                                     mempool_size=tx.mempool_size)
                else:
                    tx_node = G.add_node(tx_id, block=tx.block_height, tx_hash=tx.hash,
                                     gravity_x=gravity_x, confirmation_mins=tx.confirmation_mins,
                                     fee_per_byte=tx.fee_per_byte, type='tx')
            else:
                tx_node = G.add_node(tx_id, block=tx.block_height, tx_hash=tx.hash,
                                     gravity_x=gravity_x, type='tx')
            
            inputs = tx.inputs
            for inp in inputs:
                node_type = 'input'
                if hasattr(inp, 'address'):
                    input_id = "i" + tx_id + ":" + str(inp.address) + ":" + str(inp.n)
                    addr = inp.address
                else:
                    # Coinbase
                    node_type = 'coinbase'
                    addr = 'c0'+ str(tx.block_height)
                    input_id = addr
                    era = (tx.block_height/COINBASE_ERA_LENGTH) + 1
                    inp.value = 5000000000/era

                size = Graph.scale_size(inp.value, size_list)
                
                prev = Graph.get_previous(addr, addrHistory)
                input_node = G.add_node(input_id, size=size, address=addr, value=inp.value,
                                        gravity_x=gravity_x, type=node_type)
                G.add_edge(input_id, tx_id, weight=tx_in_weight)
                if prev is not None:
                    G.add_edge(prev, input_id, weight=addr_weight)
        
                Graph.add_history(addr, input_id, addrHistory)
            
            outputs = tx.outputs
            for out in outputs:
                output_id = "o" + tx_id + ":" + str(out.address) + ":" + str(out.n)
                addr = out.address
                if addr is not None:
                    prev = Graph.get_previous(addr, addrHistory)
                else:
                    addr = "Unknown:" + str(out.tx_index) + ":" + str(out.n)

                size = Graph.scale_size(out.value, size_list)
                

                output_node = G.add_node(output_id, size=size, gravity_x=gravity_x,
                                         value=out.value, address=addr, type='output')
                G.add_edge(tx_id, output_id, weight=tx_out_weight)
                if prev is not None:
                    G.add_edge(prev, output_id, weight=addr_weight)
                
                Graph.add_history(out.address, output_id, addrHistory)

        #print("Avg Size: " + str(sum(size_list)/float(len(sizes))))
        #print("Max Size: " + str(max(size_list)))
        #print("Min Size: " + str(min(size_list)))
        G = Graph.colour_transaction_graph(G, highlight)
        return G

#   Transaction Graph with linked transactions to view coin history/origin
    @staticmethod
    def get_trace_graph(transactions):
        G = nx.Graph()
        nodes = {}
        for tx in transactions:
            tx_id = str(tx.tx_index)
            tx_node = G.add_node(tx_id)

            inputs = tx.inputs
            for inp in inputs:
                if hasattr(inp, 'address'):
                    node = str(inp.tx_index) + ":" + str(inp.n)
                else:
                    node = "c" + tx_id

                inp_node = Graph.get_node(G, nodes, node)
                G.add_edge(tx_id, node, weight=tx_in_weight)

            outputs = tx.outputs
            for out in outputs:
                node = str(out.tx_index) + ":" + str(out.n)
                out_node = Graph.get_node(G, nodes, node)
                G.add_edge(tx_id, node, weight=tx_out_weight)

        G = Graph.colour_trace(G)
        return G


#   Transaction Graph Helper Functions

    @staticmethod
    def get_node(G, nodes, node):
        if node not in nodes:
            nodes[node] = G.add_node(node)
        return nodes[node]

    @staticmethod
    def get_edge_scale():
        return edge_scale

    @staticmethod
    def get_previous(addr, addrHistory):
        if addr in addrHistory:
            return addrHistory[addr]
        else:
            return None

    @staticmethod
    def add_history(addr, node_id, addrHistory):
        addrHistory[addr] = node_id

        #if addr not in addrHistory:
        #    addrHistory[addr] = []
        # 
        #addrHistory[addr].append(node_id)        

    @staticmethod
    def scale_size(value, list):
        if value > 0:
            size = math.log(float(value))/scaling_constant
            list.append(size)
            #print(str(size) + ":" + str(value))
            return size
            
        return 0

#  Colouring functions for generated graphs

    @staticmethod
    def colour_transaction_graph(G, highlight=None):
        G = Graph.colour_nodes(G, highlight)

        edges = G.edges_iter()
        for u, v in edges:
            colour = None
            
            u_type = G.node[u]['type']
            v_type = G.node[v]['type']

            if highlight and (highlight in v and highlight in u):
                colour = 'light_red'
            elif ((u_type == 'tx' and v_type == 'input') 
                or (v_type == 'tx' and u_type == 'input')):
                colour = 'orange'
            elif ((u_type== 'tx' and v_type == 'output')
                or (v_type == 'tx' and u_type == 'output')):
                colour = 'blue'    
            else:
                # Same address link
                if v_type == 'input' and u_type =='input':
                    colour = 'lighter_orange'
                elif v_type == 'output' and u_type =='output':
                    colour = 'lighter_blue'
                else:
                    colour = 'grey'
            
            Graph.colour_element(G[u][v], colour)

        return G

    @staticmethod
    def colour_trace(G):
        edges = G.edges_iter()
        u_colour = None
        v_colour = None
        edge_colour = None

        for u, v in edges:
            if u in v:
                # V is an output of U
                edge_colour = 'orange'
                v_colour = 'orange'
                u_colour = 'white'

            elif v in u:
                # U is an output of V
                edge_colour = 'orange'
                u_colour = 'orange'
                v_colour = 'white'

            elif ':' in v:
                # V input of U
                edge_colour = 'blue'
                v_colour = 'blue'
                u_colour = 'white'

            else:
                # U input of V
                edge_colour = 'blue'
                u_colour = 'blue'
                v_colour = 'white'

            if u[0] == 'c':
                u_colour = 'green'
            elif v[0] == 'c':
                v_colour = 'green'
                
            Graph.colour_element(G[u][v], edge_colour)
            Graph.colour_element(G.node[v], v_colour)
            Graph.colour_element(G.node[u], u_colour)
        return G

    @staticmethod
    def colour_element(e, colour):
        rgb = None
        if colour == 'grey':
            rgb = 204, 204, 204
        elif colour == 'orange':
            rgb = 255, 153, 51
        elif colour == 'light_orange':
            rgb = 255, 204, 153
        elif colour == 'lighter_orange':
            rgb = 255, 229, 204
        elif colour == 'white':
            rgb = 255, 255, 255
        elif colour == 'green':
            rgb = 153, 204, 204
        elif colour == 'light_green':
            rgb = 190, 253, 0
        elif colour == 'red':
            rgb = 248, 0, 0
        elif colour == 'light_red':
            rgb = 251, 127, 127
        elif colour == 'light_blue':
            rgb = 127, 153, 204
        elif colour == 'lighter_blue':
            rgb = 191, 205, 229
        else:
            # Blue
            rgb = 0, 51, 153

        red, green, blue = rgb
        
        e['r'] = red
        e['g'] = green
        e['b'] = blue

    @staticmethod
    def colour_nodes(G, highlight=None):
        nodes = G.nodes()
        for node in nodes:
            colour = None
            ntype = G.node[node]['type']

            if highlight and highlight in node:
                colour = 'red'
            elif ntype == 'input':
                # Orange
                colour = 'orange'
            elif ntype == 'output':
                # Blue
                colour = 'blue'
            elif ntype == 'tx':
                if 'confirmation_mins' in G.node[node]:
                    if G.node[node]['confirmation_mins'] < 20:
                        colour = 'light_green'
                    else:
                     colour = 'red'
                else:
                    colour = 'white'
            else:
                colour = 'green'

            Graph.colour_element(G.node[node], colour)

        return G

#   Data functions to pull information from graphs

    @staticmethod
    def get_tx_hashes(G):
        i = 0
        txs = ""
        nodes = G.nodes()
        for node in nodes:
            if G.node[node]['type'] == 'tx':
                if i > 0:
                    txs += ", "
                txs += G.node[node]['tx_hash'] 
                i += 1

        return txs, i

