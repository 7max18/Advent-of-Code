# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:45:32 2022

@author: MaxKo
"""

#Win Cons:
#3-2=1
#2-1=1
#1-3=-2
#Lose Cons:
#2-3=-1
#1-2=-1
#3-1=2
#Draw Cons:
#N-N=0

yourScore = 0
opponentScore = 0
opponentShape = 0
yourShape = 0

with open('Day2Input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            print(yourScore, opponentScore)
            break
        s1 = line[0]
        s2 = line[2]
        
        if s1 == 'A':
            opponentShape = 1
        elif s1 == 'B':
            opponentShape = 2
        elif s1 == 'C':
            opponentShape = 3
            
        opponentScore += opponentShape
        
        if s2 == 'X':
            yourShape = 1
        elif s2 == 'Y':
            yourShape = 2
        elif s2 == 'Z':
            yourShape = 3
        
        yourScore += yourShape
        
        outcome = yourShape-opponentShape
        
        if outcome == 1 or outcome == -2:
            yourScore += 6
            opponentScore += 0
        elif outcome == -1 or outcome == 2:
            yourScore += 0
            opponentScore += 6
        else:
            yourScore += 3
            opponentScore += 3
