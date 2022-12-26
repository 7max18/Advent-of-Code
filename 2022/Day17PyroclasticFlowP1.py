# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 18:23:08 2022

@author: MaxKo
"""

fallCount = 2022

with open('Input/Day14Input.txt') as f:
    for i in range(0, fallCount):
        wind = f.read(1)
        if not wind:
            f.seek(0)
            wind = f.read(1)
