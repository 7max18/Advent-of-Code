# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:20:25 2022

@author: MaxKo
"""

import numpy as np

TARGET_ROW = 2000000

def GetEdges(sensor, distance):
    equations = list()
    equations.append(([1, 1], sensor[0] + sensor[1] + distance))
    equations.append(([-1, 1], -sensor[0] + sensor[1] + distance))
    equations.append(([1, -1], sensor[0] - sensor[1] + distance))
    equations.append(([-1, -1], -sensor[0] - sensor[1] + distance))
    return equations

def GetIntersections(edges, sensor, distance):
    solutions = list()
    pair = list()
    firstLine = edges[0]
    secondLine = ([0, 1], TARGET_ROW)
    A = np.array([firstLine[0], secondLine[0]], dtype='int64')
    B = np.array([firstLine[1], secondLine[1]], dtype='int64')
    pair.append(tuple(np.linalg.solve(A,B).astype('int64')))
    firstLine = edges[1]
    A = np.array([firstLine[0], secondLine[0]], dtype='int64')
    B = np.array([firstLine[1], secondLine[1]], dtype='int64')
    pair.append(tuple(np.linalg.solve(A,B).astype('int64')))
    solutions.append(pair)
    pair = list()
    firstLine = edges[2]
    A = np.array([firstLine[0], secondLine[0]], dtype='int64')
    B = np.array([firstLine[1], secondLine[1]], dtype='int64')
    pair.append(tuple(np.linalg.solve(A,B).astype('int64')))
    firstLine = edges[3]
    A = np.array([firstLine[0], secondLine[0]], dtype='int64')
    B = np.array([firstLine[1], secondLine[1]], dtype='int64')
    pair.append(tuple(np.linalg.solve(A,B).astype('int64')))
    solutions.append(pair)
    for pair in solutions:
        for point in pair:
            pointDistance = abs(sensor[0] - point[0]) + abs(sensor[1] - point[1])
            if pointDistance > d:
                solutions.remove(pair)
                break
    if solutions:
        solutions = solutions[0]
        solutions.sort()
    return solutions, 0

def GetRange(sensor, distance):
    intersection = set()
    if sensor[1] - distance <= TARGET_ROW and sensor[1] + distance >= TARGET_ROW:
        dy = TARGET_ROW - sensor[1]
        dx = distance - abs(dy)
        for x in range (-dx, dx+1):
            intersection.add(sensor[0] + x)
    return intersection
        
areaMap = list()

with open('Input/Day15Input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.split(' ')
        x1 = int(''.join(filter(lambda i: i.isdigit() or i == '-', line[2])))
        y1 = int(''.join(filter(lambda i: i.isdigit() or i == '-', line[3])))
        x2 = int(''.join(filter(lambda i: i.isdigit() or i == '-', line[8])))
        y2 = int(''.join(filter(lambda i: i.isdigit() or i == '-', line[9])))
        areaMap.append(((x1, y1), (x2, y2)))

ruledOut = set()

for SBPair in areaMap:
    d = abs(SBPair[0][0] - SBPair[1][0]) + abs(SBPair[0][1] - SBPair[1][1])
    #sensorRange = GetRange(SBPair[0], d)
    if TARGET_ROW not in range(SBPair[0][1] - d, SBPair[0][1] + d + 1):
        continue
    edges = GetEdges(SBPair[0], d)
    intersections, side = GetIntersections(edges, SBPair[0], d)
    ruledOut.update(set(range(intersections[0][0], intersections[1][0] + 1)) - set([ x[1][0] for x in areaMap if x[1][1] == TARGET_ROW]))

print(len(ruledOut))
    