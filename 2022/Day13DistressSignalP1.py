# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 10:56:00 2022

@author: MaxKo
"""

def OrderCheck(left, right):  
    for elem in range(0, min(len(left), len(right))):
        if type(left[elem]) is int and type(right[elem]) is int:
            if left[elem] > right[elem]:
                return -1
            elif left[elem] < right[elem]:
                return 1
            else:
                continue
        elif type(left[elem]) is list and type(right[elem]) is list:
            if OrderCheck(left[elem], right[elem]) == 1:
                return 1
            elif OrderCheck(left[elem], right[elem]) == -1:
                return -1
            else:
                continue
        elif type(left[elem]) is list and type(right[elem]) is int:
            if OrderCheck(left[elem], [right[elem]]) == 1:
                return 1
            elif OrderCheck(left[elem], [right[elem]]) == -1:
                return -1
            else:
                continue
        elif type(left[elem]) is int and type(right[elem]) is list:
            if OrderCheck([left[elem]], right[elem]) == 1:
                return 1
            elif OrderCheck([left[elem]], right[elem]) == -1:
                return -1
            else:
                continue
    if len(left) < len(right):
        return 1
    elif len(left) > len(right):
        return -1
    else:
        return 0

def ParseList(l):
    stack = []
    num = ''
    for char in range(0, len(l)):
        if l[char].isdigit():
            num += l[char]  
        elif num != '':
            stack[len(stack) - 1].append(int(num))
            num = ''
        if l[char] == '[':
            stack.append([])
        elif l[char] == ']':
            nested = stack.pop()
            if stack != []:
                stack[len(stack) - 1].append(nested)
            else:
                stack = nested
    return stack

index = 1
correctPackets = []
with open('Input/Day13Input.txt') as f:
    while True:
        leftLine = f.readline().strip()
        rightLine = f.readline().strip()
        if OrderCheck(ParseList(leftLine), ParseList(rightLine)) == 1:
            correctPackets.append(index)
        index += 1
        line = f.readline()
        if not line:
            break

checkSum = 0
for packet in correctPackets:
    checkSum += packet

print(checkSum)