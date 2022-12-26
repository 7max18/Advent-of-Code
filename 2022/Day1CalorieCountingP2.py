# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 12:59:53 2022

@author: MaxKo
"""

topThree = [0, 0, 0]
total = 0

def TopThreeCheck():
    i = 3
    for elem in topThree[::-1]:
        i -= 1
        if total > elem:
            for j in range(0, i):
                topThree[j] = topThree[j+1]
            topThree[i] = total
            break

with open('Day1Input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            TopThreeCheck()
            print(topThree[0]+topThree[1]+topThree[2])
            break
        elif line == '\n':
            TopThreeCheck()
            total = 0
        else:
            total += int(line)