from utility import *
from decomposition import highway_decomposition
import csv

INF = 1000000000000000000000000000000000


def build_graph(file):
    # read graph
    # each line should contain two vertices, travel time and geometrical length
    # treat a graph as an undirected graph

    with open(file) as tsvfile:

        graph = {}

        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            tmp = row[0].split()

            if (int(tmp[0]) in graph):
                graph[int(tmp[0])].append([int(tmp[1]), int(tmp[2]), float(tmp[3])])
            else:
                graph[int(tmp[0])] = [[int(tmp[1]), int(tmp[2]), float(tmp[3])]]
            if (int(tmp[1]) in graph):
                graph[int(tmp[1])].append([int(tmp[0]), int(tmp[2]), float(tmp[3])])
            else:
                graph[int(tmp[1])] = [[int(tmp[0]), int(tmp[2]), float(tmp[3])]]

    return graph

def build_graph_2(file):
    # read graph
    # each line should contain two vertices, travel time and geometrical length
    # treat a graph as an undirected graph
    # Used to read the dataset USA_little_graph

    with open(file, 'r') as tsvfile:

        graph = {}

        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            if (int(row[0]) in graph):
                graph[int(row[0])].append([int(row[1]), int(row[2]), float(row[3])])
            else:
                graph[int(row[0])] = [[int(row[1]), int(row[2]), float(row[3])]]

    return graph

def query(v, pij, label):
    # calculate the distance between v and pij in according to the information in label L

    query = []

    if (label[v] == [] or label[pij] == []):
        return INF

    else:

        for element in label[v]:
            for element2 in label[pij]:
                if (element.path == element2.path):
                    sum = element.dist_node + abs(element2.dist_origin - element.dist_origin) + element2.dist_node
                    query.append(sum)
    return min(query)


def dist_from_node(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)

    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = next_node[1] + weight_to_current_node
            if next_node[0] not in shortest_paths:
                shortest_paths[next_node[0]] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node[0]][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node[0]] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return len(path) - 1


def pruned_dijkstra_search(graph, P, label, i):
    # make a dijkstra search from the vertices in P
    # each step upgrade the label or prune the search

    q = tris_priority_queue()

    for element in P:
        q.insert(tris(0, element, element))

    new_label = label

    while not q.isEmpty():
        current = q.delete()
        if query(current.v, current.pij, new_label) <= current.delta:
            continue
        new_label[current.v].append(label_t(i, dist_from_node(graph, P[0], current.pij), current.delta))
        for list in graph[current.v]:
            q.insert(tris(current.delta + 1, list[0], current.pij))

    return new_label


def preprocess(graph, example, p):
    # graph is a dicionary where the keys are the verticies of the graph
    # start the Pruned Highway Labeling 

    label = {new_list: [] for new_list in range(len(graph.keys()))}

    for i in range(0, len(p)):
        label = pruned_dijkstra_search(graph, p[i], label, i + 1)

    return label


def print_label(label):
    # simple function: print the label 
    for node in label.keys():
        print(str(node))
        print()
        for list in label[node]:
            print(str(list.path) + " - " + str(list.dist_origin) + " - " + str(list.dist_node))
        print()
