# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:55:44 2022

@author: MaxKo
"""

containerCount = 0

with open('Input/Day4Input.txt') as f:
    while True:
        pair = f.readline().strip();
        if not pair:
            print(containerCount)
            break
        assignments = pair.split(',')
        as1 = assignments[0].split('-')
        as2 = assignments[1].split('-')
        
        a1 = [int(as1[0]), int(as1[1])]
        a2 = [int(as2[0]), int(as2[1])]
        if a1[1] - a1[0] > a2[1] - a2[0]:
            if a1[0] <= a2[0] and a1[1] >= a2[1]:
                containerCount += 1
        else:
            if a1[0] >= a2[0] and a1[1] <= a2[1]:
                containerCount += 1