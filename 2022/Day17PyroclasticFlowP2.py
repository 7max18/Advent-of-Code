# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 18:23:08 2022

@author: MaxKo
"""
import copy

def GetTower(winds, wind_start, shape_start, chamber_start, peaks_start, offset):
    w = wind_start
    chamber = chamber_start
    shapeIndex = shape_start
    height = len(chamber)
    peaks = peaks_start

    #Next rock falls
    chamber.extend(copy.deepcopy(buffer))
    chamber.extend(copy.deepcopy(shapes[shapeIndex]))
    lowerBound = len(chamber) - len(shapes[shapeIndex])
    upperBound = len(chamber)

    if shapeIndex in (0, 3, 4):
        rock_count = 4
    else:
        rock_count = 5

    while True:
        #Wind push
        wind = winds[w]
        rocks = 0
        if wind == '<':
            if LeftWindCheck(chamber, lowerBound, upperBound):
                for row in range(lowerBound, upperBound):
                    for column in range(0, len(chamber[0])):
                        if chamber[row][column] == 2:
                            chamber[row][column - 1] = 2
                            chamber[row][column] = 0
                            rocks += 1
                    if rocks == rock_count:
                        break
                    
        elif wind == '>':
            if RightWindCheck(chamber, lowerBound, upperBound):
                for row in range(lowerBound, upperBound):
                    for column in range(len(chamber[0]) - 1, -1, -1):
                        if chamber[row][column] == 2:
                            chamber[row][column + 1] = 2
                            chamber[row][column] = 0
                        if rocks == rock_count:
                            break
        w += 1
        if w == len(winds):
            w = 0

        rocks = 0

        if LandedCheck(chamber, lowerBound, upperBound):
            for row in range(lowerBound, upperBound):
                for column in range(0, len(chamber[0])):
                    if chamber[row][column] == 2:
                        chamber[row][column] = 1
                        rocks += 1
                if rocks == rock_count:
                    break
            if upperBound > height:
                height = upperBound
            chamber = chamber[:height]
            break
        else:
            for row in range(lowerBound, upperBound):
                for column in range(0, len(chamber[0])):
                    if chamber[row][column] == 2:
                        chamber[row - 1][column] = 2
                        chamber[row][column] = 0
                        rocks += 1
                if rocks == rock_count:
                    break
            lowerBound -= 1
            upperBound -= 1

    for row in range(offset, len(chamber)):
        for column in range(0, len(chamber[0])):
            if chamber[row][column] == 1:
                peaks[column] = row + 1 - offset
    if SmoothCheck(chamber, offset):
        offset += min(peaks)
        for i in range(len(peaks)):
            peaks[i] -= offset

    shapeIndex += 1
    if shapeIndex == len(shapes):
        shapeIndex = 0

    return height, w, shapeIndex, chamber, peaks, offset

def LeftWindCheck(chamber, lowerBound, upperBound):
    for row in range(lowerBound, upperBound):
        for column in range(0, len(chamber[0])):
            if chamber[row][column] == 2:
                if column == 0:
                    return False
                elif chamber[row][column - 1] == 1:
                    return False
    return True

def RightWindCheck(chamber, lowerBound, upperBound):
    for row in range(lowerBound, upperBound):
        for column in range(0, len(chamber[0])):
            if chamber[row][column] == 2:
                if column == len(chamber[0]) - 1:
                    return False
                elif chamber[row][column + 1] == 1:
                    return False
    return True

def LandedCheck(chamber, lowerBound, upperBound):
    for row in range(lowerBound, upperBound):
        for column in range(0, len(chamber[0])):
            if chamber[row][column] == 2:
                if row == 0 or chamber[row - 1][column] == 1:
                    return True
    return False

#Only consider straight segments connected to the walls
def SmoothCheck(chamber, start):
    check = [False, False, False, False, False, False, False]
    for row in chamber[start:]:
        if row[0] == 1:
            r = range(len(row))
            for i in r:
                if row[i] == 1:
                    check[i] = True
                else:
                    break
        if row[len(row) - 1] == 1:
            r = reversed(range(len(row)))
            for i in r:
                if row[i] == 1:
                    check[i] = True
                else:
                    break
    for c in check:
        if not c:
            return False
    else:
        return True

fallCount = 1000000000000

shapes = [[[0, 0, 2, 2, 2, 2, 0]],
          [[0, 0, 0, 2, 0, 0, 0],
           [0, 0, 2, 2, 2, 0, 0],
           [0, 0, 0, 2, 0, 0, 0]],
          [[0, 0, 2, 2, 2, 0, 0],
           [0, 0, 0, 0, 2, 0, 0],
           [0, 0, 0, 0, 2, 0, 0]],
          [[0, 0, 2, 0, 0, 0, 0],
           [0, 0, 2, 0, 0, 0, 0],
           [0, 0, 2, 0, 0, 0, 0],
           [0, 0, 2, 0, 0, 0, 0]],
          [[0, 0, 2, 2, 0, 0, 0],
           [0, 0, 2, 2, 0, 0, 0]]
         ]

buffer = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]

with open('Input/Day17Input.txt') as f:
    winds = f.readline()

count = 1
states = list()
h = 0
cycles = list()
inits = list()

wind = 0
shape = 0
peaks = [0, 0, 0, 0, 0, 0, 0]
offset = 0
ground = list()
heights = list()
offset = 0

while True:
    height, wind, shape, ground, peaks, offset = GetTower(winds, wind, shape, ground, peaks, offset)
    heights.append(height)
    states.append((tuple(peaks), wind, shape))
    if len(set(states)) < len(states):
        indices = [i for i,c in enumerate(states) if c==states[-1]]
        init = indices[-2]
        cycle = len(states) - 1 - init
        if init + cycle > fallCount:
            print(heights[fallCount - 1])
            break
        i_height = heights[init]
        h = (heights[cycle+init] - i_height) * ((fallCount - init) // cycle) + heights[init + ((fallCount - init) % cycle) - 1]
        print(h)
        break
    count += 1
