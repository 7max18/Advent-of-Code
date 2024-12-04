import re
import math

memory = ""

with open('input.txt') as f:
    for line in f.readlines():
        memory += line

muls = re.findall('mul[(]\d+,\d+[)]', memory)
total = 0
for instr in muls:
    total += math.prod([int(x) for x in re.findall('\d+', instr)])

print(total)