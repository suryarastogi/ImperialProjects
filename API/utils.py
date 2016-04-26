class Utils(object):

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