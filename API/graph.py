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
    def get_transaction_graph(transactions):
        G = nx.Graph()

        addrHistory = {}
        size_list = []
        for tx in transactions:
            
            tx_id = "tx" + str(tx.tx_index)
            
            tx_node = G.add_node(tx_id)
            
            inputs = tx.inputs
            for inp in inputs:
                color = 'orange'
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
                input_node = G.add_node(input_id, size=size)#, color=color)
                G.add_edge(input_id, tx_id, color=color, weight=tx_in_weight)
                if prev is not None:
                    G.add_edge(prev, input_id, weight=addr_weight)#, color='gray')
        
                Graph.add_history(addr, input_id, addrHistory)
            
            outputs = tx.outputs
            for out in outputs:
                output_id = "o" + tx_id + ":" + str(out.address) + ":" + str(out.n)
                addr = out.address
                size = Graph.scale_size(out.value, size_list)
                
                prev = Graph.get_previous(addr, addrHistory)
                output_node = G.add_node(output_id, size=size)#, color='blue')
                G.add_edge(tx_id, output_id, weight=tx_out_weight)#, color='blue')
                if prev is not None:
                    G.add_edge(prev, output_id, weight=addr_weight)#, color='gray')
                
                Graph.add_history(out.address, output_id, addrHistory)

        #print("Avg Size: " + str(sum(size_list)/float(len(sizes))))
        #print("Max Size: " + str(max(size_list)))
        #print("Min Size: " + str(min(size_list)))
        return G

    @staticmethod
    def colour_transaction_graph(G):
        nodes = G.nodes()
        for node in nodes:
            colour = None
            ntype = Graph.node_type(node)
            if ntype == 'input':
                # Orange
                G.node[node]['r'] = 255
                G.node[node]['g'] = 200
                G.node[node]['b'] = 0
            elif ntype == 'output':
                # Blue
                G.node[node]['r'] = 0
                G.node[node]['g'] = 0
                G.node[node]['b'] = 255
            elif ntype == 'tx':
                G.node[node]['r'] = 255
                G.node[node]['g'] = 255
                G.node[node]['b'] = 255
            else:
                G.node[node]['r'] = 0
                G.node[node]['g'] = 255
                G.node[node]['b'] = 0

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
                colour = 'grey'
            
            if colour == 'grey':
                #Grey
                G[u][v]['r'] = 137
                G[u][v]['g'] = 137
                G[u][v]['b'] = 137
            elif colour == 'orange':
                #Orange
                G[u][v]['r'] = 255
                G[u][v]['g'] = 200
                G[u][v]['b'] = 0
            else:
                #Orange
                G[u][v]['r'] = 0
                G[u][v]['g'] = 0
                G[u][v]['b'] = 255

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

