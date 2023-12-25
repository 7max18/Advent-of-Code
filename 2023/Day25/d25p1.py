import random
import copy
import math
from itertools import combinations
import time

#Adapted from https://github.com/cshjin/MinCutAlgo

def MinCut(graph):
    group_sizes = {edge: set([edge]) for edge in graph}
    while len(graph) > 2:
        start = random.choice(list(graph.keys()))
        finish = random.choice(graph[start])
        # print start, finish
        # # Adding the edges from the absorbed node:
        for edge in graph[finish]:
            if edge != start:  # this stops us from making a self-loop
                graph[start].append(edge)
                    #print(t, halves)
                            
        # # Deleting the references to the absorbed node and changing them to the source node:
        for edge in graph[finish]:
            graph[edge].remove(finish)
            if edge != start:  # this stops us from re-adding all the edges in start.
                graph[edge].append(start)
                if edge in graph[start]:
                    group_sizes[start].update(group_sizes[finish])
                
        del graph[finish]
        del group_sizes[finish]

    # # Calculating and recording the mincut
    mincut = graph[list(graph.keys())[0]]
    sizes = list(group_sizes.values())
    if len(mincut) == 3 and sizes[0].symmetric_difference(sizes[1]) == set(main_graph.keys()):
        cuts.add(frozenset({len(x) for x in sizes}))

main_graph = {}
global cuts
cuts = set()
edge_num = 0
edge_list = []

start_time = time.time()
with open("Day25Input.txt") as f:
    for line in f.readlines():
        node = line.split()[0][:-1]
        edges = []
        if node not in main_graph:
            main_graph[node] = list()
        for edge in line.split()[1:]:
            edges.append(edge)
            if edge not in main_graph:
                main_graph[edge] = list()
            if node not in main_graph[edge]:
                main_graph[edge].append(node)
        main_graph[node] += edges
        edge_num = edge_num + len(edges)
        edge_list.append(len(edges))

for i in range(200):
    graph1 = copy.deepcopy(main_graph)
    MinCut(graph1)

sizes = list(list(cuts)[0])
print(sizes[0]*sizes[1])