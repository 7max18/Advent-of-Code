# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 00:09:32 2022

@author: MaxKo
"""

MAX_DIR_SIZE = 100000

dSizes = dict()
path = []
dirIndex = 0
with open('Input/Day7Input.txt') as f:
    while True:
        tline = f.readline().strip().split(' ')
        if tline == ['']:
            break
        if tline[0] == '$' :
            if tline[1] == 'cd':
                if tline[2] == '..':
                    path.pop()
                else:
                    path.append(dirIndex)
                    dSizes[dirIndex] = 0
                    dirIndex += 1
        elif tline[0] != 'dir':
            for d in path:
                if d in dSizes:
                    dSizes[d] += int(tline[0])
                    if dSizes[d] > MAX_DIR_SIZE:
                        del dSizes[d]

sizeSum = 0

for s in dSizes.values():
    sizeSum += s
    
print(sizeSum)
    