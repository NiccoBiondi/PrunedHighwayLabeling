import matplotlib.pyplot as plt
import networkx as nx

# simple python program to plot a graph
# is used to save the graph images used in presentation


G = nx.Graph()
pos = nx.spring_layout(G)

node = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
edge = [(0, 3), (0, 5), (0, 6), (0, 8), (0, 11), (0, 9), (0, 7), (3, 5), (5, 6), (6, 8), (8, 11), (11, 2), (2, 10),
        (10, 9), (9, 1), (1, 7), (1, 4), (7, 4), (4, 3)]

G.add_nodes_from(node)

G.add_edges_from(edge)

final_path = [[0, 3, 4, 1], [5, 6], [11, 2, 10, 9], [8], [7]]

color_map = []
color_map_2 = []

for nodes in node:
    if nodes in final_path[0]:
        color_map.append('orange')
    elif nodes in final_path[1]:
        color_map.append('skyblue')
    elif nodes in final_path[2]:
        color_map.append('lightgreen')
    elif nodes in final_path[3]:
        color_map.append('yellow')
    else:
        color_map.append('pink')

for nodes in node:
    if nodes in final_path[0]:
        color_map_2.append('orange')
    else:
        color_map_2.append('deepskyblue')


pos = {0: (30, 30), 1: (35, 20), 2: (28, -4), 3: (31, 50), 4: (34, 40), 5: (28, 50), 6: (26, 40), 7: (33, 30),
       8: (25, 25), 9: (32, 13), 10: (31, -9), 11: (27, 12)}

#nx.draw_networkx(G, pos=pos, node_size=1000, node_color='deepskyblue', with_labels=True)
#nx.draw_networkx(G, pos=pos, node_size=1000, node_color=color_map, with_labels=True)
nx.draw_networkx(G, pos=pos, node_size=1000, node_color=color_map_2, with_labels=True)


plt.axis('off')
plt.savefig('graph_decomposed.png')
plt.show()
