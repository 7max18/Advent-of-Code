def hash(step):
    code = 0
    for char in step:
        code += ord(char)
        code *= 17
        code %= 256
    return code

with open("Input/Day15Input.txt") as f:
    sequence = f.readline().strip().split(",")

checksum = 0
for step in sequence:
    checksum += hash(step)
print(checksum)