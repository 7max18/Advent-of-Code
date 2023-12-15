# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:20:25 2022

@author: MaxKo
"""
import numpy as np
from itertools import combinations

MAX_COORD = 4000000

def GetEdges(sensor, distance):
    equations = list()
    equations.append(([1, 1], sensor[0] + sensor[1] + distance))
    equations.append(([-1, 1], -sensor[0] + sensor[1] + distance))
    equations.append(([1, -1], sensor[0] - sensor[1] + distance))
    equations.append(([-1, -1], -sensor[0] - sensor[1] + distance))
    return equations
    
def GetIntersections(firstBorder, secondBorder):
    solutions = list()
    firstLine = firstBorder[0]
    secondLine = secondBorder[1]
    A = np.array([firstLine[0], secondLine[0]], dtype='int64')
    B = np.array([firstLine[1], secondLine[1]], dtype='int64')
    solutions.append(tuple(np.linalg.solve(A,B).astype('int64')))
    firstLine = firstBorder[2]
    secondLine = secondBorder[3]
    A = np.array([firstLine[0], secondLine[0]], dtype='int64')
    B = np.array([firstLine[1], secondLine[1]], dtype='int64')
    solutions.append(tuple(np.linalg.solve(A,B).astype('int64')))
    firstLine = firstBorder[2]
    secondLine = secondBorder[0]
    A = np.array([firstLine[0], secondLine[0]], dtype='int64')
    B = np.array([firstLine[1], secondLine[1]], dtype='int64')
    solutions.append(tuple(np.linalg.solve(A,B).astype('int64')))
    firstLine = firstBorder[1]
    secondLine = secondBorder[3]
    A = np.array([firstLine[0], secondLine[0]], dtype='int64')
    B = np.array([firstLine[1], secondLine[1]], dtype='int64')
    solutions.append(tuple(np.linalg.solve(A,B).astype('int64')))
    return solutions

def InRangeCheck(point, sensors):
    if point[0] < 0 or point[0] > MAX_COORD or point[1] < 0 or point[1] > MAX_COORD:
        return False
    for sensor in sensors:
        pointDistance = abs(sensor[0][0] - point[0]) + abs(sensor[0][1] - point[1])
        signalRange = abs(sensor[0][0] - sensor[1][0]) + abs(sensor[0][1] - sensor[1][1])
        if pointDistance <= signalRange:
            return False
    return True
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

signalBorders = []
candidates = set([(0, 0), (0, MAX_COORD), (MAX_COORD, MAX_COORD), (MAX_COORD, 0)])
for SBPair in areaMap:
    d = 1 + abs(SBPair[0][0] - SBPair[1][0]) + abs(SBPair[0][1] - SBPair[1][1])
    signalBorders.append(GetEdges(SBPair[0], d))

for system in list(combinations(signalBorders, 2)):
    candidates.update(GetIntersections(system[0], system[1]))
    
for candidate in candidates:
    if InRangeCheck(candidate, areaMap):
        tuningFrequency = candidate[0] * MAX_COORD + candidate[1]
        break

print(tuningFrequency)