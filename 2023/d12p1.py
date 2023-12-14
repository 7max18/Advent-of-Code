def get_solutions(row, clues, pos=0, counter=0, clue_index=0):
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
                return 0
            counter += 1
            if counter > clues[clue_index]:
                return 0
        elif condition == "?":
            damaged = get_solutions(row[:row_index]+"#"+row[row_index+1:], clues, row_index, counter, clue_index)
            operational = get_solutions(row[:row_index]+"."+row[row_index+1:], clues, row_index, counter, clue_index)
            return sum([damaged,operational])
    else:
        if counter > 0 and counter == clues[clue_index]:
            clue_index += 1
        if clue_index == len(clues):
            return 1
        else:
            return 0
with open("Input/Day12Input.txt") as f:
    springs = list()
    for line in f.readlines():
        springs.append([line.split()[0], eval("["+line.split()[1]+"]")])
solutions = list()
for row, clues in springs:
    solutions.append(get_solutions(row,clues))
print(sum(solutions))
