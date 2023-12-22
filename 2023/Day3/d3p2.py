def scan_for_parts(schematic, xpos, ypos):
    parts = list()
    if ypos > 0:
        top = schematic[ypos-1]
        mark = -1
        for i, char in list(enumerate(top))[xpos-1:xpos+2]:
            if i < mark:
                continue
            if char.isdigit():
                part, mark = extract_part(top, i)
                parts.append(part)
    if ypos < len(schematic) - 1:
        bottom = schematic[ypos+1]
        mark = -1
        for i, char in list(enumerate(bottom))[xpos-1:xpos+2]:
            if i < mark:
                continue
            if char.isdigit():
                part, mark = extract_part(bottom, i)
                parts.append(part)
    if xpos > 0:
        left = schematic[ypos][xpos-1]
    if xpos < len(schematic[0]) - 1:
        right = schematic[ypos][xpos+1]
    if left.isdigit():
        part, pos = extract_part(schematic[ypos], xpos-1)
        parts.append(part)
    if right.isdigit():
        part, pos = extract_part(schematic[ypos], xpos+1)
        parts.append(part)
    return parts

def extract_part(row, start):
    part_num = str()
    pos = start
    while pos > 0 and row[pos-1].isdigit():
        pos -= 1
    while pos < len(row) and row[pos].isdigit():
        part_num += row[pos]
        pos += 1
    return int(part_num), pos
with open("Day3Input.txt") as f:
    schematic = [line.strip() for line in f.readlines()]

gears = list()
for i, y in enumerate(schematic):
    mark = -1
    for j, x in enumerate(y):
        if x == "*":
            gears.append(scan_for_parts(schematic, j, i))
            
ratios = list()
for gear in gears:
    if len(gear) == 2:
        ratios.append(gear[0] * gear[1])

print(sum(ratios))