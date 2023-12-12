def scan_for_symbols(schematic, xpos, ypos):
    top = str()
    bottom = str()
    left = str()
    right = str()
    if ypos > 0:
        top = schematic[ypos-1][xpos-1:xpos+2]
    if ypos < len(schematic) - 1:
        bottom = schematic[ypos+1][xpos-1:xpos+2]
    if xpos > 0:
        left = schematic[ypos][xpos-1]
    if xpos < len(schematic[0]) - 1:
        right = schematic[ypos][xpos+1]
    for char in top+bottom+left+right:
        if not char.isdigit() and char != ".":
            return True
    return False

def extract_part(row, start):
    part_num = str()
    pos = start
    while pos > 0 and row[pos-1].isdigit():
        pos -= 1
    while pos < len(row) and row[pos].isdigit():
        part_num += row[pos]
        pos += 1
    return int(part_num), pos

with open("Input/Day3Input.txt") as f:
    schematic = [line.strip() for line in f.readlines()]

parts = list()
for i, y in enumerate(schematic):
    mark = -1
    for j, x in enumerate(y):
        if x.isdigit():
            if j < mark:
                continue
            part_num, end_pos = extract_part(y, j)
            if scan_for_symbols(schematic, j, i):
                parts.append(part_num)
                mark = end_pos

print(sum(parts))