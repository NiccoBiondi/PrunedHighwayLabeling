# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph

import sys  # Library for INT_MAX


class Graph():

    def __init__(self, adiacen_matrix, V):
        self.V = V
        self.graph = adiacen_matrix

    def minKey(self, key, mstSet):

        # Initilaize min value
        min = sys.maxsize
        min_index = 0

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def childhood(self, parent):
        childhood = {new_list: [] for new_list in range(self.V)}
        for i in range(self.V):#mi indicano i padri
            for j in range(len(parent)): # trovo i figli del padre i
                if (parent[j] == i ):
                    childhood[i].append(j)

        return childhood

    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self, node):

        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[node] = 0
        mstSet = [False] * self.V

        parent[node] = -1  # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        childhood = self.childhood(parent)

        return parent, childhood

    def update_matrix(self, adiacent_matrix):
        self.graph = adiacent_matrix


