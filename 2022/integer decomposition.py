# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 14:19:12 2022

@author: MaxKo
"""

clues = {
    1: "Works like Mr.",
    2: "Prize",
    3: "Cut",
    4: "Cape",
    5: "Quaff",
    6: "Parties with",
    7: "Rescues or",
    8: "Docs",
    9: "Larva",
    10: "Vittles or",
    11: "Religious",
    12: "One might go for laxer",
    13: "Flags or sails",
    14: "Containers of beer",
    15: "Pyramid creator",
    16: "Teaching",
    17: "Opening",
    18: "Derogatory nickname for",
    19: "Gleason's sitcom",
    20: "Seals",
    21: "Or chap",
    22: "Coverings",
    23: "Daughter",
    24: "Remove from one's",
    25: "Mechanical",
    26: "Titanic",
    27: "Sidestepping",
    28: "Galway, etc.",
    29: "Pact",
    30: "Dye",
    31: "To Clytemnestra",
    32: "Lizard, AKA",
    33: "Novelties",
    34: "It may be presented under",
    35: "Follower of",
    36: "Preprandial",
    37: "Products like bad",
    38: "The Louvre",
    39: "James",
    40: "Spring",
    41: "Angela's country",
    42: "An anaesthesiologist",
    43: "Destroyer and others",
    44: "Puns",
    45: "Creature",
    46: "Married",
    47: "Wife",
    48: "Like elephant",
    49: "Digs",
    50: "Banknote",
    51: "Rug",
    52: "Series with Aries",
    53: "March",
    54: "Or subsequently",
    55: "Because",
    56: "Holland's",
    57: "Footballer",
    58: "Parcels",
    59: "Festival of",
    60: "Senhor",
    61: "Downtown theatre",
    62: "Not having",
    63: "Company",
    64: "Pakistani",
    65: "Sore",
    66: "Cemetery",
    67: "Glass",
    68: "Florida",
    69: "Patented in 1758",
    70: "Roof",
    71: "Spits",
    72: "Corn",
    73: "Zork",
    74: "Preserves",
    75: "Lots"
    }
 
# Array to store the numbers used
# to form the required sum
dp = [0 for i in range(200)]
count = 0

# Function to print the array which contains
# the unique partitions which are used
# to form the required sum
def print1(idx, count):
    repeats = False
    exclude = [1, 2, 4, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25,
               26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48, 49, 50,
               52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 70, 72, 73, 74, 75]
    include = []
    for number in dp[1:idx]:
        if number in exclude:
            repeats = True
            break
        else:
            exclude.append(number)
    if repeats == False and (include == [] or all(item in dp for item in include)):
        for i in range(1, idx, 1):
            print(clues[dp[i]],end = " ")
        print("\n", end = "")
        
 
# Function to find all the unique partitions
# remSum = remaining sum to form
# maxVal is the maximum number that
# can be used to make the partition
def solve(remSum,maxVal,idx = 1,count = 0):        
    if count > 9:
        return
    # If remSum == 0 that means the sum
    # is achieved so print the array
    if (remSum == 0):
        print1(idx, count)
        return
    # i will begin from maxVal which is the
    # maximum value which can be used to form the sum
    i = maxVal
    while(i >= 1):
        if (i > remSum):
            i -= 1
        elif (i <= remSum):
            # Store the number used in forming
            # sum gradually in the array
            dp[idx] = i
            
            # Since i used the rest of partition
            # cant have any number greater than i
            # hence second parameter is i
            solve(remSum - i, i, idx + 1, count + 1)
            i -= 1
     
# This code is contributed by
# Surendra_Gangwar


solve(int(input()), maxVal = 25)
