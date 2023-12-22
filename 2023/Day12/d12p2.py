def get_solutions(row, clues, pos=0, clue_pos=0, counter=0):
    if (pos, clue_pos, counter, row[pos]) in ways:
        return ways[(pos, clue_pos, counter, row[pos])]
    clue_index = clue_pos
    start_count = counter
    for row_index, condition in list(enumerate(row))[pos:]:
        if condition == ".":
            if counter > 0:
                if counter == clues[clue_index]:
                    counter = 0
                    clue_index += 1
                else:
                    return 0
        elif condition == "#":
            if clue_index == len(clues):
                ways[(pos, clue_pos, start_count, row[pos])] = 0
                return 0
            counter += 1
            if counter > clues[clue_index]:
                ways[(pos, clue_pos, start_count, row[pos])] = 0
                return 0
        elif condition == "?":
            operational = get_solutions(row[:row_index]+"."+row[row_index+1:], clues, row_index, clue_index, counter)
            ways[(row_index, clue_index, counter, ".")] = operational
            damaged = get_solutions(row[:row_index]+"#"+row[row_index+1:], clues, row_index, clue_index, counter)
            ways[(row_index, clue_index, counter, "#")] = damaged
            return damaged + operational
    else:
        if counter > 0 and counter == clues[clue_index]:
            clue_index += 1
        if clue_index == len(clues):
            ways[(pos, clue_pos, start_count, row[pos])] = 1
            return 1
        else:
            ways[(pos, clue_pos, start_count, row[pos])] = 0
            return 0
 
with open("Day12Input.txt") as f:           
    springs = list()
    for line in f.readlines():
        springs.append(["?".join([line.split()[0] for i in range(5)]), eval("("+",".join([line.split()[1] for i in range(5)])+")")])
total = 0
for row, clues in springs:
    ways = dict()
    total += get_solutions(row, clues)
print(total)
