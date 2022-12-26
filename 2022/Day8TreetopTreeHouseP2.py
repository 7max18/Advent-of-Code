# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 00:33:34 2022

@author: MaxKo
"""
def TreeScan(t, r, c, rt, ct):
    nScore = 0
    sScore = 0
    wScore = 0
    eScore = 0
    
    for treeIndex in range(r - 1, -1, -1):
        nScore += 1
        if int(trees[treeIndex][c]) >= t:
            break
    for treeIndex in range(r + 1, rt):
        sScore += 1
        if int(trees[treeIndex][c]) >= t:
            break
    for treeIndex in range(c - 1, -1, -1):
        wScore += 1
        if int(trees[r][treeIndex]) >= t:
            break
    for treeIndex in range(c + 1, ct):
        eScore += 1
        if int(trees[r][treeIndex]) >= t:
            break
    return nScore * sScore * wScore * eScore
    

trees = []

with open('Input/Day8Input.txt') as f:
    while True:
        treeline = f.readline().strip()
        if not treeline:
            break
        trees.append(treeline)

rows = len(trees)
columns = len(trees[0])
maxScore = 0
for row in range(0, rows):
    for column in range(0, columns):
        if row == 0 or row == rows - 1 or column == 0 or column == columns - 1:
            continue
        else:
            score = TreeScan(int(trees[row][column]), row, column, rows, columns)
            if score > maxScore:
                maxScore = score

print(maxScore)