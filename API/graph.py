import networkx as nx

api_key = "87575b65-eb36-4322-a0a1-43c2b705479f"

class Graph(object):

    edge_scale = 5
    addr_weight = 30
    tx_out_weight = 1*edge_scale #5
    tx_in_weight = 4*edge_scale #20

    scaling_constant = 26.00/10.00 # 1.00 #12.5460737323 #Average from test block

    @staticmethod
    def getEdgeScale():
        return edge_scale

    @staticmethod
    def getPrevious(addr, addrHistory):
        if addr in addrHistory:
            # Last element in history
            return addrHistory[addr][-1]
        else:
            return None

    @staticmethod
    def addHistory(addr, node_id, addrHistory):
        if addr not in addrHistory:
            addrHistory[addr] = []
        
        addrHistory[addr].append(node_id)        

    @staticmethod
    def scale_size(value, list):
        if value > 0:
            size = math.log(float(value))/scaling_constant
            list.append(size)
            print(str(size) + ":" + str(value))
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
                size = scale_size(inp.value, size_list)
                
                prev = getPrevious(addr, addrHistory)
                input_node = G.add_node(input_id, size=size)#, color=color)
                G.add_edge(input_id, tx_id, color=color, weight=tx_in_weight)
                if prev is not None:
                    G.add_edge(prev, input_id, weight=addr_weight)#, color='gray')
        
                addHistory(addr, input_id, addrHistory)
            
            outputs = tx.outputs
            for out in outputs:
                output_id = "o" + tx_id + ":" + str(out.address) + ":" + str(out.n)
                addr = out.address
                size = scale_size(out.value, size_list)
                
                prev = getPrevious(addr, addrHistory)
                output_node = G.add_node(output_id, size=size)#, color='blue')
                G.add_edge(tx_id, output_id, weight=tx_out_weight)#, color='blue')
                if prev is not None:
                    G.add_edge(prev, output_id, weight=addr_weight)#, color='gray')
                
                addHistory(out.address, output_id, addrHistory)

        #print("Avg Size: " + str(sum(size_list)/float(len(sizes))))
        #print("Max Size: " + str(max(size_list)))
        #print("Min Size: " + str(min(size_list)))
        return G