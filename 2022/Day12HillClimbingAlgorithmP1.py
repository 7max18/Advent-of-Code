# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 11:10:15 2022

@author: MaxKo
"""

from colorama import Fore
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def Heuristic(node):
    dist = abs(end[0] - node[0]) + abs(end[1] - node[1])
    remainingClimb = heightMap[end[0]][end[1]] - heightMap[node[0]][node[1]]
    return dist + pow(remainingClimb, 2)

def CanAddToOpen(o, node, f):
    if node in o:
        if f >= fScore[node]:
            return False
    return True
    
def ReconstructPath(history, cur):
    totalPath = [cur]
    while cur in history.keys():
        cur = history[cur]
        if cur == start:
            break
        totalPath.insert(0, cur)
    X = []
    Y = []
    for coord in totalPath:
        X.append(coord[1])
        Y.append(coord[0])
    heatMap = np.array(heightMap)
    mpl.rcParams['font.family'] = 'Avenir'
    mpl.rcParams['font.size'] = 18
    mpl.rcParams['axes.linewidth'] = 2
    fig = plt.figure(figsize=(heatMap.shape[0],heatMap.shape[1]))
    ax = fig.add_subplot()
    ax.plot(X, Y, color = 'black', linewidth = 5)
    ax.imshow(heatMap, origin='lower', cmap='RdYlGn_r', vmin=0, vmax=26)
    # for row in range(0, len(heightMap)):
    #     string = ''
    #     for column in range(0, len(heightMap[0])):
    #         if (row, column) in totalPath:
    #             string += Fore.RED + chr(heightMap[row][column] + 64) 
    #         else:
    #             string += Fore.RESET + chr(heightMap[row][column] + 96) 
    #     print(string)
    return len(totalPath)
    
heightMap = []
start = tuple()
end = tuple()
row = 0
column = 0
nodes = []

with open('Input/Day12Input.txt') as f:
    while True:
        line = f.readline().strip()
        if not line or line == ['']:
            break
        heightRow = []
        for square in line:
            if square == 'S':
                start = (row, column)
                heightRow.append(1)
            elif square == 'E':
                end = (row, column)
                heightRow.append(26)
            else:
                heightRow.append(ord(square) - 96) 
            column += 1
        heightMap.append(heightRow)
        row += 1
        column = 0


#A*

openSet = [start]
closedSet = []
cameFrom = dict()
gScore = dict()
fScore = dict()
gScore[start] = 0
fScore[start] = Heuristic(start)

while openSet != []:
    current = openSet[0]
    if current == end:
        print(ReconstructPath(cameFrom, current))
        break
    openSet.remove(current)
    closedSet.append(current)
    neighbors = []
    if current[0] > 0:
        neighbors.append((current[0]-1, current[1]))
    if current[0] < len(heightMap) - 1:
        neighbors.append((current[0]+1, current[1]))
    if current[1] > 0:
        neighbors.append((current[0], current[1]-1))
    if current[1] < len(heightMap[0]) - 1:
        neighbors.append((current[0], current[1]+1))
    for neighbor in neighbors:
        if neighbor in closedSet or heightMap[neighbor[0]][neighbor[1]] - heightMap[current[0]][current[1]] > 1:
            continue
        tentativeG = gScore[current] + 1
        tentativeF = tentativeG + Heuristic(neighbor)
        if CanAddToOpen(openSet, neighbor, tentativeF):
            cameFrom[neighbor] = current
            gScore[neighbor] = tentativeG
            fScore[neighbor] = tentativeF
            if openSet == []:
                openSet.append(neighbor)
            else:
                for i, value in enumerate(openSet):
                    if fScore[value] > fScore[neighbor] and neighbor not in openSet:
                        openSet.insert(i, neighbor)
                        break
                
            
        