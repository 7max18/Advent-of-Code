# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 00:33:34 2022

@author: MaxKo
"""
def TreeScan(t, r, c, rt, ct):
    visibleFromWest = True
    visibleFromEast = True
    visibleFromNorth = True
    visibleFromSouth = True
    
    for treeIndex in range(r - 1, -1, -1):
        if int(trees[treeIndex][c]) >= t:
            visibleFromNorth = False
            break
    for treeIndex in range(r + 1, rt):
        if int(trees[treeIndex][c]) >= t:
            visibleFromSouth = False
            break
    for treeIndex in range(c - 1, -1, -1):
        if int(trees[r][treeIndex]) >= t:
            visibleFromWest = False
            break
    for treeIndex in range(c + 1, ct):
        if int(trees[r][treeIndex]) >= t:
            visibleFromEast = False
            break
    if visibleFromNorth or visibleFromSouth or visibleFromWest or visibleFromEast:
        return 1
    else:
        return 0
    

trees = []

with open('Input/Day8Input.txt') as f:
    while True:
        treeline = f.readline().strip()
        if not treeline:
            break
        trees.append(treeline)

rows = len(trees)
columns = len(trees[0])
visibleTrees = 0
for row in range(0, rows):
    for column in range(0, columns):
        if row == 0 or row == rows - 1 or column == 0 or column == columns - 1:
            visibleTrees += 1
        else:
            visibleTrees += TreeScan(int(trees[row][column]), row, column, rows, columns)

print(visibleTrees)