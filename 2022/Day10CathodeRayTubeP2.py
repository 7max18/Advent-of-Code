# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 00:05:01 2022

@author: MaxKo
"""
pixelCounter = 0
X = 1
screen = ['.'*40] * 6

def Tick(cycles):
    global pixelCounter
    while cycles > 0:
        pixel = pixelCounter % 40
        if pixel >= X-1 and pixel <= X+1:
            CRTLine = screen[pixelCounter // 40]
            screen[pixelCounter // 40] = CRTLine[:pixel] + '#' + CRTLine[pixel + 1:]
        pixelCounter += 1
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

for line in screen:
    print(line)