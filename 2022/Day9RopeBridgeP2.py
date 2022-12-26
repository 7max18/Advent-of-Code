# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 00:08:06 2022

@author: MaxKo
"""

def CheckKnotProx(headDisp, i):
    dx = int(abs(headDisp[0]))
    dy = int(abs(headDisp[1]))
    if dx <= 1 and dy <= 1:
        return
    elif (dx + dy) % 2 == 0:
        rope[i][0] += int(headDisp[0] / 2)
        rope[i][1] += int(headDisp[1] / 2)
    else:
        if dx > dy:
            rope[i][0] += int(headDisp[0] / 2)   
            rope[i][1] += headDisp[1]
        else:
            rope[i][0] += headDisp[0]  
            rope[i][1] += int(headDisp[1] / 2)  
    
    if i == 9:
        VisitedCheck(rope[9])
        return
    else:
        CheckKnotProx((rope[i][0] - rope[i+1][0], rope[i][1] - rope[i+1][1]), i+1)
    
def VisitedCheck(t):
    pos = (t[0],t[1])
    if not pos in tailPoints:
        tailPoints.append(pos)

tailPoints = [(0,0)]
rope = []

for i in range(0, 10):
    rope.append([0,0])

with open('Input/Day9Input.txt') as f:
    while True:
        line = f.readline().strip().split(' ')
        if not line or line == ['']:
            break
        steps = int(line[1])
        for step in range(0, steps):
            initPos = []
            if line[0] == 'R':
                rope[0][0] += 1
            elif line[0] == 'L':
                rope[0][0] -= 1
            elif line[0] == 'U':
                rope[0][1] += 1
            elif line[0] == 'D':
                rope[0][1] -= 1
            CheckKnotProx((rope[0][0] - rope[1][0], rope[0][1] - rope[1][1]), 1)

print(len(tailPoints))
            
