# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:20:25 2022

@author: MaxKo
"""

TARGET_ROW = 2000000

def GetRange(sensor, distance):
    intersection = set()
    if sensor[1] - distance <= TARGET_ROW and sensor[1] + distance >= TARGET_ROW:
        dy = TARGET_ROW - sensor[1]
        dx = distance - abs(dy)
        for x in range (-dx, dx+1):
            intersection.add(sensor[0] + x)
    return intersection
        
areaMap = []

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
    sensorRange = GetRange(SBPair[0], d)
    for loc in sensorRange:
        if (loc, TARGET_ROW) not in [ x[1] for x in areaMap ]:
            ruledOut.add(loc)

print(len(ruledOut))
    