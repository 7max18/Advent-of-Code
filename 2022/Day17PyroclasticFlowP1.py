# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 18:23:08 2022

@author: MaxKo
"""
import copy

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
                if row == 0:
                    return True
                elif chamber[row - 1][column] == 1:
                    return True
    return False
    
fallCount = 290 + 1755

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

height = 0

chamber = []

shapeIndex = 0

with open('Input/Day17Input.txt') as f:
    for i in range(fallCount):
        #Next rock falls
        chamber.extend(copy.deepcopy(buffer))
        chamber.extend(copy.deepcopy(shapes[shapeIndex]))
        lowerBound = height + 3
        upperBound = len(chamber)
        while True:
            #Wind push
            wind = f.read(1)
            if not wind:
                f.seek(0)
                wind = f.read(1)
            if wind == '<':
                if LeftWindCheck(chamber, lowerBound, upperBound):
                    for row in range(lowerBound, upperBound):
                        for column in range(0, len(chamber[0])):
                            if chamber[row][column] == 2:
                                chamber[row][column - 1] = 2
                                chamber[row][column] = 0
            elif wind == '>':
                if RightWindCheck(chamber, lowerBound, upperBound):
                    for row in range(lowerBound, upperBound):
                        for column in range(len(chamber[0])-1, -1, -1):
                            if chamber[row][column] == 2:
                                chamber[row][column + 1] = 2
                                chamber[row][column] = 0
            #Check if can fall any more
            if LandedCheck(chamber, lowerBound, upperBound):
                for row in range(lowerBound, upperBound):
                    for column in range(0, len(chamber[0])):
                        if chamber[row][column] == 2:
                            chamber[row][column] = 1
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
                lowerBound -= 1
                upperBound -= 1
        shapeIndex += 1
        if shapeIndex == len(shapes):
            shapeIndex = 0

print(height)