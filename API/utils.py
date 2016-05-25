import untangle
import math
import networkx as nx
from graph import Graph
from celery.task.control import discard_all

class Utils(object):

    @staticmethod
    def fix_gephi_graphml(graph_path):
        G = nx.read_graphml(graph_path)
        G = Graph.colour_transaction_graph(G)
        nx.write_graphml(G, graph_path)
        Utils.fix_xml(graph_path)

    # General fix for graphml inconsistencies between
    # networkX, gephi, and GDO graph app
    @staticmethod
    def fix_xml(graph_path):
        obj = untangle.parse(graph_path)
        replace = []
        replacements = {}
        # Replaces ids such as "d10" to actual attributes, ex "size"
        for key in obj.graphml.key:
            name = '"' + key['attr.name'] + '"' 
            key_id = '"' + key['id'] + '"' 
            name.replace(" ", "")

            replacements[key_id] = name
            replace.append(key_id)

        lines = []
        with open(graph_path) as infile:
            #For strict ordering
            for line in infile:
                for src in replace:
                    line = line.replace(src, replacements[src])
                lines.append(line)
        with open(graph_path, 'w') as outfile:
            for line in lines:
                outfile.write(line)

    @staticmethod
    def get_mins_between(start, end):
        return float(math.fabs(start-end))/float(60)

    @staticmethod
    def is_mins_after(start, end, mins=30):
        return math.fabs(start-end) > (mins*60)

    # Graph Naming Functions
    @staticmethod
    def get_trace_tx_viz_file_name(id):
        return "TraceTx" + str(id) + ".graphml"

    @staticmethod
    def get_address_viz_file_name(id):
        return "Address" + str(id) + ".graphml"

    @staticmethod
    def get_block_viz_file_name(id):
        return "BlockViz" + str(id) + ".graphml"

    @staticmethod
    def get_block_viz_sub_file_name(id, subid):
        return "BlockViz" + str(id) + "C" + str(subid) + ".graphml"