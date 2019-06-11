from pruned_highway_labeling import *

from decomposition import highway_decomposition


# This represent the graph in the paper
#file = "/home/bazza/Scrivania/labeledgraph/Code/database/joke_tree.tsv"

# This represent the graph created for the presentation
file = "/home/bazza/Scrivania/labeledgraph/Code/database/example_graph.tsv"

# This represent a portion of real dataset used in paper
#file = "/home/bazza/Scrivania/labeledgraph/Code/database/USA_example_graph.tsv"


# use two different function to build graph because the file was written differently
if "joke_tree" in file or "example_graph" in file:
    graph = build_graph(file)
else:
    graph = build_graph_2(file)



# make the highway decomposition of the input graph
highway = highway_decomposition(file, len(graph.keys()))

print(highway)

# create the label
label = preprocess(graph, file, highway)

print_label(label)

print("Printing query....")
print(query(5, 8, label))


