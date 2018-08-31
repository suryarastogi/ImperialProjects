import networkx as nx

def getPrevious(addr, addrHistory):
    if addr in addrHistory:
        # Last element in history
        return addrHistory[addr][-1]
    else:
        return None

def addHistory(addr, node_id, addrHistory):
    if addr not in addrHistory:
        addrHistory[addr] = []
    
    addrHistory[addr].append(node_id)        

def populateGraph(G, transactions, debug=False): 
    addrHistory = {}
       
    for tx in transactions:
        tx_id = "tx" + str(tx.tx_index)
        
        tx_node = G.add_node(tx_id)
        
        inputs = tx.inputs
        for inp in inputs:
            if hasattr(inp, 'address'):
                input_id = "i" + tx_id + ":" + str(inp.address) + ":" + str(inp.n)
                addr = inp.address
            else:
                # Coinbase
                input_id = "0"
                addr = 0
                
            prev = getPrevious(addr, addrHistory)
            input_node = G.add_node(input_id, color='orange')
            G.add_edge(input_id, tx_id, color='orange')
            if prev is not None:
                G.add_edge(prev, input_id, color='gray')
    
            addHistory(addr, input_id, addrHistory)
        
        outputs = tx.outputs
        for out in outputs:
            output_id = "o" + tx_id + ":" + str(out.address) + ":" + str(out.n)
            output_node = G.add_node(output_id, color='blue')
            G.add_edge(tx_id, output_id, color='blue')
            addHistory(out.address, output_id, addrHistory)

    return G

def layoutGraph(G):
    pos = nx.spring_layout(G, iterations=50, scale=10)
    #pos = nx.graphviz_layout(G, prog='fdp')
    #pos = nx.graphviz_layout(G, prog='sfdp')
    
    
    return pos

def print_log(msg, debug):
    if debug:
        print(msg)
    else:
        pass