# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 21:20:25 2022

@author: MaxKo
"""

bufferLength = 0
sopWindow = ['']*14

with open('Input/Day6Input.txt') as f:
    while True:
        c = f.read(1)
        bufferLength += 1
        if c == '':
            print("Uh oh!")
            break
        for i in range(0, 13):
            sopWindow[i] = sopWindow[i+1]
        sopWindow[13] = c
        if len(sopWindow) == len(set(sopWindow)) and not '' in sopWindow:
            print(bufferLength)
            break