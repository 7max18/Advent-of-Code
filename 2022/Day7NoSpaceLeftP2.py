# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 00:09:32 2022

@author: MaxKo
"""

MAX_USED_SPACE = 40000000

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
                dSizes[d] += int(tline[0])

totalSize = dSizes[0]

sortedSizes = dict(sorted(dSizes.items(), key=lambda x:x[1]))

for s in sortedSizes.values():
    reducedSpace = totalSize - s
    if reducedSpace < MAX_USED_SPACE:
        print(s)
        break
    