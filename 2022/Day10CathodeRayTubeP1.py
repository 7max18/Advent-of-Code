# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 00:05:01 2022

@author: MaxKo
"""
cycleCounter = 1
interestingCycle = 20
cycleIndex = 0
X = 1
strengthSum = 0

def Tick(cycles):
    global cycleCounter, strengthSum, interestingCycle
    while cycles > 0:
        if cycleCounter == interestingCycle:
            strengthSum += cycleCounter * X
            interestingCycle += 40
        cycleCounter += 1
        cycles -= 1

with open('Input/Day10Input.txt') as f:
    while True:
        line = f.readline().strip().split(' ')
        if not line or line == ['']:
            break
        if line[0] == 'noop':
            Tick(1)
        elif line[0] == 'addx':
            Tick(2)
            X += int(line[1])

print(strengthSum)