# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 12:43:56 2022

@author: MaxKo
"""

max = 0
sum = 0
done = False

with open('Day1Input.txt') as f:
    while not done:
        line = f.readline()
        if not line:
            print(max)
            break
        elif line == '\n':
            if sum > max:
                max = sum
            sum = 0
        else:
            sum += int(line)
        
        
        