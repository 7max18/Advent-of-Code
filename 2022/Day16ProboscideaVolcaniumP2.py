# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:33:48 2022

@author: MaxKo
"""

from itertools import combinations

def BFS(root, goal, matrix):
    pathLevels = [ 0 for i in range(0, len(matrix)) ]
    queue = [root]
    pathLevels[root] = 1
    while queue is not []:
        vertex = queue.pop(0)
        if vertex == goal:
            return pathLevels[vertex]
        for index, value in enumerate(matrix[vertex]):
            if value == 1 and pathLevels[index] == 0:
                queue.append(index)
                pathLevels[index] = pathLevels[vertex] + 1

def GetMaxPressure(root, time, nodes, explored, pathLengths):
    unseen = set(nodes) - set(explored)
    readings = []
    for node in unseen:
        t = time - pathLengths[frozenset([root, node])]
        if t < 0:
            continue
        else:
            seen = explored.union(set([node]))
            score = node[1] * t
            newPaths = GetMaxPressure(node, t, nodes, seen, pathLengths)
            for new in newPaths:
                readings.append((new[0] + score, [node[0]] + new[1]))
    if readings != []:
        return readings
    else:
        return [(0, [])]
        
def SearchScores(scoresList):
    max = 0
    for i in range(0, len(scoresList)):
        score1 = scoresList[i][0]
        for j in range(i, len(scoresList)):
            score2 = scoresList[j][0]
            potentialScore = score1 + score2
            if potentialScore < max:
                break
            elif potentialScore > max and set(scoresList[i][1]).isdisjoint(set(scoresList[j][1])):
                max = potentialScore
    return max

valves = []
tunnels = []
adjMatrix = []

with open('Input/Day16Input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.split(' ')
        valveLabel =''.join(filter(lambda i: i.isalpha(), line[1]))
        flowRate = int(''.join(filter(lambda i: i.isdigit() or i == '-', line[4])))
        tunnelLabels = []
        for i in range(9, len(line)):
            tunnelLabels.append(''.join(filter(lambda a: a.isalpha(), line[i])))
        valve = (valveLabel, flowRate)
        valves.append(valve)
        tunnels.append(tunnelLabels)

valveLabels = [ v[0] for v in valves ]

for v in range(0, len(valves)):
    adjMatrix.append([ 0 for i in range(0, len(valves))])
    for tunnel in tunnels[v]:
        adjMatrix[v][valveLabels.index(tunnel)] = 1

start = [(i, v) for i, v in enumerate(valves) if v[0] == 'AA'][0]
workingValves = [(i, v) for i, v in enumerate(valves) if v[1] > 0 or v[0] == 'AA']

tunnelLengths = dict()

for tunnel in list(combinations(workingValves, 2)):
    tunnelLengths[frozenset([tunnel[0][1], tunnel[1][1]])] = BFS(tunnel[0][0], tunnel[1][0], adjMatrix)

workingValves = [a[1] for a in workingValves]
start = start[1]

remainingTime = 26
visited = set()

scores = GetMaxPressure(start, remainingTime, set(workingValves) - set([('AA', 0)]), visited, tunnelLengths)
scores.sort(reverse=True)
maxScore = SearchScores(scores)
print(maxScore)

