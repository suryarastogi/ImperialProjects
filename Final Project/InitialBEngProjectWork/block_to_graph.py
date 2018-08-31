from blockchain import blockexplorer
import matplotlib.pyplot as plt
import networkx as nx

import data_source as data
import graph_utils as GraphUtils

transactions = data.getTransactions()

G = nx.Graph()

GraphUtils.populateGraph(G, transactions)

print("Transactions: " + str(len(transactions)))
'''
print("Laying out graph...")
pos = GraphUtils.layoutGraph(G)

# For GraphML
#for node, (x,y) in pos.items():
#    G.node[node]['x'] = str(float(x))
#    G.node[node]['y'] = str(float(y))    

print("Filtering Nodes: ")
#outputs = [node for node in G.nodes() if node.startswith("o")]
#inputs = [node for node in G.nodes() if node.startswith("i")]
#txs = [node for node in G.nodes() if node.startswith("tx")]
                       
print("Drawing Inputs: ")
nx.draw_networkx_nodes(G,pos,
                       nodelist=inputs,
                       node_color='orange',
                       node_size=500,
                       alpha=0.8)        

print("Drawing Transactions: ")
nx.draw_networkx_nodes(G,pos,
                       nodelist=txs,
                       node_color='black',
                       node_size=100,
                       alpha=0.8)

print("Drawing Outputs: ")
nx.draw_networkx_nodes(G,pos,
                       nodelist=outputs,
                       node_color='blue',
                       node_size=500,
                       alpha=0.8)
          
print("Drawing Edges: ")             
nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)

#nx.draw(G,pos)
'''
nx.write_graphml(G, "three.graphml")
#plt.show()
