import re

num_dict = {"one":1,
            "two":2,
            "three":3,
            "four":4,
            "five":5,
            "six":6,
            "seven":7,
            "eight":8,
            "nine":9,
            "zero":0}

calibration_value = 0
with open("Input/Day1Input.txt") as f:
    for line in f.readlines():
        for char in line:
            if char.isdigit():
                first = 10*int(char)
                break
            elif [re.search(line, num) for num in num_dict]:
                last = 10*num_dict[[re.search(line, num).group() for num in num_dict][0]]
        for char in line[::-1]:
            if char.isdigit():
                last = char
                break
            elif [re.search(line[:], num) for num in num_dict]:
                last = num_dict[[re.search(line, num).group() for num in num_dict][0]]
        calibration_value += first+last
        
print(calibration_value)