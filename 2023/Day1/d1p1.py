calibration_value = 0
with open("Day1Input.txt") as f:
    for line in f.readlines():
        for char in line:
            if char.isdigit():
                first = char
                break
        for char in line[::-1]:
            if char.isdigit():
                last = char
                break
        calibration_value += int(first+last)
        
print(calibration_value)