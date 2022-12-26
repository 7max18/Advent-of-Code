# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:55:44 2022

@author: MaxKo
"""

crates = []
crateColumn = 0

with open('Input/Day5Input.txt') as f:
    while True:
        crateArea = f.read(4)
        if crateArea[1].isalpha():
            if len(crates) < crateColumn + 1:
                for i in range(len(crates), crateColumn + 1):
                    crates.append([])
            crates[crateColumn].append(crateArea[1])
        elif crateArea[1].isdigit():
            break
        crateColumn += 1
        if crateArea[3] == "\n":
            crateColumn = 0
    while f.read(1) != '\n':
        pass
    f.readline()
    while True:
        instruction = f.readline().strip().split(' ')
        if not instruction or instruction == ['']:
            break
        temp = crates[int(instruction[3])-1][0:int(instruction[1])]
        del crates[int(instruction[3])-1][0:int(instruction[1])]
        crates[int(instruction[5])-1] = temp + crates[int(instruction[5])-1]
            
result = ''

for i in range(0, len(crates)):
    result += crates[i][0]
    
print(result)