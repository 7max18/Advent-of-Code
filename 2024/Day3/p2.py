import re
import math

memory = ""

with open("input.txt") as f:
    for line in f.readlines():
        memory += line

instrs = re.findall(r"mul[(]\d+,\d+[)]|don\'t[(][)]|do[(][)]", memory)
total = 0
flag = True
for instr in instrs:
    if instr == "don\'t()":
        flag = False
    elif instr == "do()":
        flag = True
    else:
        if flag:
            total += math.prod([int(x) for x in re.findall("\d+", instr)])

print(total)