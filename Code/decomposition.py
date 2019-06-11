import csv
from utility import speed
import numpy as np
from prim_msp import Graph

# Python file where is made the highway decomposition of the graph


def speed_up_2(file, V):
    # calculate the speed of each edge, the degree of each node
    # and the adjacent matrix of the graph (file)
    # used for USA_little_graph 

    spd = []
    deg = [0] * V
    adiacent_matrix = np.zeros(shape=(V, V))

    with open(file) as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            spd.append(speed(int(row[0]), int(row[1]), float(row[3]) / int(row[2])))
            deg[int(row[0])] += 1
            adiacent_matrix[int(row[0])][int(row[1])] = int(row[2])


    return spd, deg, adiacent_matrix

def speed_up(file, V):
    # calculate the speed of each edge, the degree of each node
    # and the adjacent matrix of the graph (file)
    # used for joke_example and example graphs

    spd = []
    deg = [0] * V
    adiacent_matrix = np.zeros(shape=(V, V))

    with open(file) as tsvfile:
        graph = {}

        reader = csv.reader(tsvfile, delimiter='\t')
        for row in reader:
            tmp = row[0].split()
            spd.append(speed(int(tmp[0]), int(tmp[1]), float(tmp[3]) / int(tmp[2])))
            spd.append(speed(int(tmp[1]), int(tmp[0]), float(tmp[3]) / int(tmp[2])))
            deg[int(tmp[0])] += 1
            deg[int(tmp[1])] += 1
            adiacent_matrix[int(tmp[0])][int(tmp[1])] = int(tmp[2])
            adiacent_matrix[int(tmp[1])][int(tmp[0])] = int(tmp[2])

    return spd, deg, adiacent_matrix



def decompose_in_level(num_level, spd):
    # distribute each node in a level

    min_speed = 1000000000000000000000000
    max_speed = 0

    for element in spd:
        if element.speed > max_speed:
            max_speed = element.speed
        if element.speed < min_speed:
            min_speed = element.speed

    gap = (max_speed - min_speed) / num_level

    level = {new_list: [] for new_list in range(num_level)}

    for edge in spd:
        for i in range(0, num_level):

            if (min_speed + (i * gap)) <= edge.speed <= (min_speed + (i + 1) * gap):

                if not (edge.frm in level[num_level - 1 - i]):
                    level[num_level - 1 - i].append(edge.frm)

                if not (edge.to in level[num_level - 1 - i]):
                    level[num_level - 1 - i].append(edge.to)

    for i in range(0, num_level):
        for node in level[i]:
            for j in range(i + 1, num_level):
                if node in level[j]:
                    level[j].remove(node)

    return level


def take_max_deg(level, deg):
    # take max degree node in a given level

    best = level[0]

    for node in level:
        if deg[node] > deg[best]:
            best = node

    return best


def descendant(childhood, n):
    # calculate the descendant on a node in according to childhood vector
    # childhood: in position i is written the parent of i in the primMST

    descendant_node = [0] * len(childhood.keys())
    q = childhood[n]
    while (len(q) != 0):
        current = q[0]
        q = [x for x in q if x != current]
        for child in childhood[current]:
            q.append(child)
            descendant_node[current] += 1

    for node in childhood.keys():
        for child in childhood[node]:
            descendant_node[node] += descendant_node[child]

    sum = 0
    for child in childhood[n]:
        sum += descendant_node[child]

    descendant_node[n] = len(childhood[n]) + sum

    return descendant_node


def choose_path(node, childhood, descendant_node):
    # choose path in according to the number of childhood
    queue = [node]
    current = node
    while (True):
        s = []
        for node in childhood[current]:
            if abs(descendant_node[node] - descendant_node[current]) > 0.05:
                s.append(node)
        if not (len(s) == 0):
            y = s[0]
            for element in s:
                if descendant_node[element] > descendant_node[y]:
                    y = element
            current = y
            queue.append(y)
        else:
            return queue


def highway_decomposition(file, V, num_level=4):
    # make the highway decomposition with 4 level
    
    # calculate speed, degree and adjacent matrix
    if "joke_tree" in file or "example_graph" in file:
        spd, deg, adjacent_matrix = speed_up(file, V)
    else:
        spd, deg, adjacent_matrix = speed_up_2(file, V)


    # level 0 max speed, level n-1 min speed
    level = decompose_in_level(num_level, spd)
    	
    # build graph from adjacent matrix
    g = Graph(adjacent_matrix, V)

    tmp = np.zeros(shape=(V, V))

    for i in range(V):
        for j in range(V):
            tmp[i][j] = adjacent_matrix[i][j]

    highway = []
    
    # there we make the real decompositon 
    for i in range(0, num_level):
        q = level[i]
        while (len(q) != 0):
            
            node = take_max_deg(q, deg)  

            # with the prim tree we ake the parent and childhood of a node
            parent, childhood = g.primMST(node) 

            # compute the descendant for each node
            descendant_node = descendant(childhood, node)

            # we compute the path Pi of the final decomposition
            queue = choose_path(node, childhood, descendant_node)

            # delete all node in the path Pi from level and graph
            for element in queue:
                for j in range(0, num_level):
                    level[j] = [x for x in level[j] if x != element]

            q = level[i]

            for element in queue:
                for node in childhood.keys():
                    tmp[element][node] = 0
                    tmp[node][element] = 0

            g.update_matrix(tmp)

            highway.append(queue)

    return highway
