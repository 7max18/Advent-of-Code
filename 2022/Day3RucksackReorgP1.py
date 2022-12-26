# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:25:05 2022

@author: MaxKo
"""

prioritySum = 0

with open('Day3Input.txt') as f:
    while True:
        rucksack = f.readline()
        if not rucksack:
            print(prioritySum)
            break
        divider = int(len(rucksack) / 2)
        c1 = rucksack[:divider]
        c2 = rucksack[divider:]
        mistake = set(c1) & set(c2)
        for m in mistake:
            if m >= 'a':
                prioritySum += ord(m) - 96
            else:
                prioritySum += ord(m) - 38