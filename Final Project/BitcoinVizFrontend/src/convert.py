import networkx as nx
import json

def write_json_graph(G, graph_path):
    nodes = G.nodes()
    edges = G.edges_iter()

    n = []
    max_size = 0
    for node_id in nodes:
        if G.node[node_id]['size'] > max_size:
            max_size = G.node[node_id]['size'] 

    print "--Max Size: " + str(max_size)
    
    for node_id in nodes:
        node = G.node[node_id]
        node_type = node['type']

        node_obj = {}
        node_obj['id'] = node_id

        if ('confirmation_mins' in node and node['confirmation_mins'] > 20):
            node_obj['color'] = '#F00'
            node_obj['label'] = 'Tx Hash: ' + node['tx_hash']
        elif node_type == 'tx':
            node_obj['color'] = '#CF0'
            node_obj['label'] = 'Tx Hash: ' + node['tx_hash']
        elif node_type == 'output':
            node_obj['color'] = '#039'
            node_obj['label'] = 'Output to: ' + node['address']
        else:
            node_obj['color'] = '#F93' 
            node_obj['label'] = 'Input from: ' + node['address']

        node_obj['x'] = node['x']
        node_obj['y'] = node['y']
        #inode_obj['size'] = .5 #float(node['size']*scaling_constant)
        n.append(node_obj)

    e = []
    for inp, outp in edges:
        edge_obj = {}
        edge_obj['id'] = inp + "E" + outp

        if (G.node[inp]['type'] == 'input' and G.node[outp]['type'] == 'tx') or (G.node[inp]['type'] == 'tx' and G.node[outp]['type'] =='input'):
            edge_obj['color'] = '#F93'
            edge_obj['label'] = 'Input'
        elif (G.node[inp]['type'] == 'output' and G.node[outp]['type'] == 'tx') or (G.node[inp]['type'] == 'tx' and G.node[outp]['type'] =='output'):
            edge_obj['color'] = '#039'
            edge_obj['label'] = 'Output'
        else:
            edge_obj['color'] = '#CCC'
            edge_obj['label'] = 'Address Reuse'

        edge_obj['source'] = inp
        edge_obj['target'] = outp
        e.append(edge_obj)

    ret = {}
    ret['nodes'] = n
    ret['edges'] = e

    with open(graph_path, 'w') as outfile:
        json.dump(ret, outfile)
    print("JSON output: " + graph_path)

convert_id = 131
graph_path = "/Users/surya/backend/data/Coloured/BlockViz" + str(convert_id) + ".graphml"
json_path = "/Users/surya/backend/data/Coloured/BlockViz" + str(convert_id) + ".json"
G = nx.read_graphml(graph_path)
write_json_graph(G, json_path)