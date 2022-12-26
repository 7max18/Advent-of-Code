# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:17:25 2022

@author: MaxKo
"""

def SandFall():
    sandLoc = (source[0]-xMin, source[1])
    caveMap[sandLoc[1]][sandLoc[0]] = 2
    while True:
        print(sandLoc)
        if sandLoc[1] == yMax:
            return False
        
        if caveMap[sandLoc[1] + 1][sandLoc[0]] == 0:
            caveMap[sandLoc[1]][sandLoc[0]] = 0
            caveMap[sandLoc[1] + 1][sandLoc[0]] = 2
            sandLoc = (sandLoc[0], sandLoc[1] + 1)
        elif caveMap[sandLoc[1] + 1][sandLoc[0] - 1] == 0:
            caveMap[sandLoc[1]][sandLoc[0]] = 0
            caveMap[sandLoc[1] + 1][sandLoc[0] - 1] = 2
            sandLoc = (sandLoc[0] - 1, sandLoc[1] + 1)
        elif caveMap[sandLoc[1] + 1][sandLoc[0] + 1] == 0:
            caveMap[sandLoc[1]][sandLoc[0]] = 0
            caveMap[sandLoc[1] + 1][sandLoc[0] + 1] = 2
            sandLoc = (sandLoc[0] + 1, sandLoc[1] + 1)
        else:
            return True
         
        

source = (500, 0)
rocks = []
with open('Input/Day14Input.txt') as f:
    while True:
        path = f.readline()
        if not path:
            break
        path = path.split(' ')
        rock = []
        for line in path[::2]:
            rock.append((eval(line)))
        rocks.append(rock)

xMin = min([ min(x) for x in rocks ])[0] - 1
xMax = max([ max(x) for x in rocks ])[0] + 1
yMax = max([ max(x, key = lambda a:a[1]) for x in rocks ], key = lambda a:a[1])[1]

caveMap = [[0 for i in range(0, xMax-xMin+1)] for i in range(0, yMax+1)]
for rock in rocks:
    for point in range(0, len(rock)):
        caveMap[rock[point][1]][rock[point][0]-xMin] = 1
        nextPoint = point + 1
        if nextPoint == len(rock):
            break
        if rock[point][0] == rock[nextPoint][0]:
            if rock[point][1] < rock[nextPoint][1]:
                for y in range(rock[point][1], rock[nextPoint][1]):
                    caveMap[y][rock[point][0]-xMin] = 1
            else:
                for y in range(rock[nextPoint][1], rock[point][1]):
                    caveMap[y][rock[point][0]-xMin] = 1   
        else:
            if rock[point][0] < rock[nextPoint][0]:
                for x in range(rock[point][0]-xMin, rock[nextPoint][0]-xMin):
                    caveMap[rock[point][1]][x] = 1
            else:
                for x in range(rock[nextPoint][0]-xMin, rock[point][0]-xMin):
                    caveMap[rock[point][1]][x] = 1

sandCount = 0

while SandFall() == True:
    sandCount += 1
    
caveMap[source[1]][source[0]-xMin] = 3
for y in range(0, len(caveMap)):
    line = ''
    for x in range(0, len(caveMap[0])):
        if caveMap[y][x] == 0:
            line += '.'
        elif caveMap[y][x] == 1:
            line += '#'
        elif caveMap[y][x] == 2:
            line += 'o'
        elif caveMap[y][x] == 3:
            line+= '+'
    print(line)
    
print(sandCount)
                
        
        