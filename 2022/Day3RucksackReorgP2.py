# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:25:05 2022

@author: MaxKo
"""

import itertools

prioritySum = 0

with open('Day3Input.txt') as f:
    while True:
        rucksacks = list(itertools.islice(f, 3))
        if not rucksacks:
            print(prioritySum)
            break
        mistake = set(rucksacks[0].strip()) & set(rucksacks[1].strip()) & set(rucksacks[2].strip())
        for m in mistake:
            if m >= 'a':
                prioritySum += ord(m) - 96
            else:
                prioritySum += ord(m) - 38