import regex

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
        first = regex.search(r"(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(zero)|[1234567890]", line).group()
        if first in num_dict:
            first = 10*num_dict[first]
        else:
            first = 10*int(first)
        last = regex.search(r"(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(zero)|[1234567890]", line, flags=regex.REVERSE).group()
        if last in num_dict:
            last = num_dict[last]
        else:
            last = int(last)
        calibration_value += first+last
        
print(calibration_value)