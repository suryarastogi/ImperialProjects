import math
import networkx as nx

api_key = "87575b65-eb36-4322-a0a1-43c2b705479f"
edge_scale = 5
addr_weight = 30
tx_out_weight = 1*edge_scale #5
tx_in_weight = 4*edge_scale #20

scaling_constant = 26.00/10.00 # 1.00 #12.5460737323 #Average from test block

class Graph(object):

    @staticmethod
    def node_type(node):
        if node[0] == 'i':
            return 'input'
        elif node[0] == 'o':
            return 'output'
        elif node[0] == 't':
            return 'tx'
        else:
            return 'coinbase'

    @staticmethod
    def get_node(G, nodes, node):
        if node not in nodes:
            nodes[node] = G.add_node(node)
        return nodes[node]

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

    @staticmethod
    def get_edge_scale():
        return edge_scale

    @staticmethod
    def get_previous(addr, addrHistory):
        if addr in addrHistory:
            # Last element in history
            return addrHistory[addr][-1]
        else:
            return None

    @staticmethod
    def add_history(addr, node_id, addrHistory):
        if addr not in addrHistory:
            addrHistory[addr] = []
        
        addrHistory[addr].append(node_id)        

    @staticmethod
    def scale_size(value, list):
        if value > 0:
            size = math.log(float(value))/scaling_constant
            list.append(size)
            #print(str(size) + ":" + str(value))
            return size
            
        return 0

    @staticmethod
    def get_transaction_graph(transactions, highlight=None):
        G = nx.Graph()

        addrHistory = {}
        size_list = []
        for tx in transactions:
            tx_id = "tx" + str(tx.hash)
            if hasattr(tx, 'confirmation_mins'):
                tx_node = G.add_node(tx_id, block=tx.block_height, mins=tx.confirmation_mins)
            else:
                tx_node = G.add_node(tx_id, block=tx.block_height)
            
            inputs = tx.inputs
            for inp in inputs:
                if hasattr(inp, 'address'):
                    input_id = "i" + tx_id + ":" + str(inp.address) + ":" + str(inp.n)
                    addr = inp.address
                else:
                    # Coinbase
                    input_id =  "0" + tx_id
                    addr = "0" + tx_id
                    inp.value = 2500000000 #TODO update to be based on height
                size = Graph.scale_size(inp.value, size_list)
                
                prev = Graph.get_previous(addr, addrHistory)
                input_node = G.add_node(input_id, size=size, block=tx.block_height)
                G.add_edge(input_id, tx_id, weight=tx_in_weight)
                if prev is not None:
                    G.add_edge(prev, input_id, weight=addr_weight)
        
                Graph.add_history(addr, input_id, addrHistory)
            
            outputs = tx.outputs
            for out in outputs:
                output_id = "o" + tx_id + ":" + str(out.address) + ":" + str(out.n)
                addr = out.address
                size = Graph.scale_size(out.value, size_list)
                
                prev = Graph.get_previous(addr, addrHistory)
                output_node = G.add_node(output_id, size=size, block=tx.block_height)
                G.add_edge(tx_id, output_id, weight=tx_out_weight)
                if prev is not None:
                    G.add_edge(prev, output_id, weight=addr_weight)
                
                Graph.add_history(out.address, output_id, addrHistory)

        #print("Avg Size: " + str(sum(size_list)/float(len(sizes))))
        #print("Max Size: " + str(max(size_list)))
        #print("Min Size: " + str(min(size_list)))
        G = Graph.colour_transaction_graph(G, highlight)
        return G

    @staticmethod
    def colour_element(e, colour):

        if colour == 'grey':
            # Grey
            e['r'] = 204
            e['g'] = 204
            e['b'] = 204
        elif colour == 'orange':
            #rgb = (255, 153, 51)
            #Orange
            e['r'] = 255
            e['g'] = 153
            e['b'] = 51
        elif colour == 'white':
            e['r'] = 255
            e['g'] = 255
            e['b'] = 255
        elif colour == 'green':
            e['r'] = 153
            e['g'] = 204
            e['b'] = 204
        elif colour == 'light_green':
            e['r'] = 190
            e['g'] = 253
            e['b'] = 0
        elif colour == 'red':
            e['r'] = 248
            e['g'] = 0
            e['b'] = 0
        else:
            # Blue
            e['r'] = 0
            e['g'] = 51
            e['b'] = 153

        #red, green, blue = rgb
        
        #e['r'] = red
        #e['g'] = green
        #e['b'] = blue
    @staticmethod
    def colour_nodes(G, highlight=None):
        nodes = G.nodes()
        for node in nodes:
            colour = None
            ntype = Graph.node_type(node)
            if highlight and highlight in node:
                colour = 'red'
            elif ntype == 'input':
                # Orange
                colour = 'orange'
            elif ntype == 'output':
                # Blue
                colour = 'blue'
            elif ntype == 'tx':
                if 'mins' in G.node[node]:
                    if G.node[node]['mins'] < 20:
                        colour = 'light_green'
                    else:
                     colour = 'red'
                else:
                    colour = 'white'
            else:
                colour = 'green'

            Graph.colour_element(G.node[node], colour)
        return G

    @staticmethod
    def colour_transaction_graph(G, highlight=None):
        G = Graph.colour_nodes(G, highlight)

        edges = G.edges_iter()
        for u, v in edges:
            colour = None
        
            if Graph.node_type(u) == 'tx':
                if Graph.node_type(v) == 'input':
                    colour = 'orange'
                else:
                    colour = 'blue'    
            elif Graph.node_type(v) == 'tx':
                if Graph.node_type(u) == 'input':
                    colour = 'orange'
                else:
                    colour = 'blue'
            else:
                if highlight and highlight in v:
                    colour = 'green'
                else:
                    colour = 'grey'
            
            Graph.colour_element(G[u][v], colour)

        return G

    @staticmethod
    def get_tx_index(node):
        return node.split('tx')[1]

    @staticmethod
    def get_tx_indexes(G):
        i = 0
        txs = ""
        nodes = G.nodes()
        for node in nodes:
            if Graph.node_type(node) == 'tx':
                if i > 0:
                    txs += ", "
                txs += Graph.get_tx_index(node) 
                i += 1

        return txs, i

