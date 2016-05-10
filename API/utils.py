import untangle

class Utils(object):
    # General fix for graphml errors parsing by Gephi
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

    # Graph Naming Functions
    @staticmethod
    def get_address_viz_file_name(id):
        return "Address" + str(id) + ".graphml"

    @staticmethod
    def get_block_viz_file_name(id):
        return "BlockViz" + str(id) + ".graphml"

    @staticmethod
    def get_block_viz_sub_file_name(id, subid):
        return "BlockViz" + str(id) + "C" + str(subid) + ".graphml"

    @staticmethod
    def fix_graphml(graph_path):
        replacements = {'d10':'g', 'd11':'weight', 'd0':'size', 'd1':'b', 'd2':'g', 'd3':'y', 'd4':'x', 'd5':'r', 
                    'd6':'label', 'd7':'edgeid', 'd8':'r', 'd9':'b'}
        lines = []
        with open(graph_path) as infile:
            #For strict ordering
            replace = ['d10', 'd11', 'd0', 'd1', 'd2','d3', 'd4', 'd5', 'd6', 'd7','d8', 'd9']
            for line in infile:
                for src in replace:
                    line = line.replace(src, replacements[src])
                lines.append(line)
        with open(graph_path, 'w') as outfile:
            for line in lines:
                outfile.write(line)