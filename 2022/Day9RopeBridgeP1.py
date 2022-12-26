# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 00:08:06 2022

@author: MaxKo
"""

def CheckTailProx(h, t):
    if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
        return True
    else:
        return False
    
def VisitedCheck(t):
    pos = (t[0],t[1])
    if not pos in tailPoints:
        tailPoints.append(pos)

headPos = [0,0]
tailPos = [0,0]
tailPoints = [(0,0)]

with open('Input/Day9Input.txt') as f:
    while True:
        line = f.readline().strip().split(' ')
        if not line or line == ['']:
            break
        steps = int(line[1])
        
        if line[0] == 'R':
            for step in range(0, steps):
                headPos[0] += 1
                if CheckTailProx(headPos, tailPos):
                    tailPos[0] = headPos[0] - 1
                    tailPos[1] = headPos[1]
                    VisitedCheck(tailPos)
        elif line[0] == 'L':
            for step in range(0, steps):
                headPos[0] -= 1
                if CheckTailProx(headPos, tailPos):
                    tailPos[0] = headPos[0] + 1
                    tailPos[1] = headPos[1]
                    VisitedCheck(tailPos)
        elif line[0] == 'U':
            for step in range(0, steps):
                headPos[1] += 1
                if CheckTailProx(headPos, tailPos):
                    tailPos[0] = headPos[0]
                    tailPos[1] = headPos[1] - 1
                    VisitedCheck(tailPos)
        elif line[0] == 'D':
            for step in range(0, steps):
                headPos[1] -= 1
                if CheckTailProx(headPos, tailPos):
                    tailPos[0] = headPos[0]
                    tailPos[1] = headPos[1] + 1
                    VisitedCheck(tailPos)
                    
print(len(tailPoints))
                    

        
        
