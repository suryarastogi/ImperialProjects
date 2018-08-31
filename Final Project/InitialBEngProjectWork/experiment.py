from blockchain import blockexplorer

from pygraphml import Graph
from pygraphml import GraphMLParser

latestblock = blockexplorer.get_latest_block()
transactions = latestblock.tx_indexes

print("Len: " + str(len(transactions)))

for t in transactions[:100]:
    tx = blockexplorer.get_tx(str(t))
    inputs = tx.inputs
    ouputs = tx.outputs
    print(t)
    for inp in inputs:
        if hasattr(inp, 'address'): 
            print(inp.address)
        else:
            print(inp.script_sig)
    
g = Graph()

n1 = g.add_node("A")
n2 = g.add_node("B")
n3 = g.add_node("C")
n4 = g.add_node("D")
n5 = g.add_node("E")

g.add_edge(n1, n3)
g.add_edge(n2, n3)
g.add_edge(n3, n4)
g.add_edge(n3, n5)

g.show()