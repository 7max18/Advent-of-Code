# Start with the clues, not the springs.

def get_solutions(row, clues):
    row = row.split(".")
    minimums = [list() for x in range(len(row))]
    for index, segment in enumerate(row):
        counter = 0
        for spring in segment:
            if spring == "#":
                counter += 1
            else:
                if counter != 0:
                    minimums[index].append(counter)
                counter = 0
    print(minimums)

    
with open("Input/Day12Input.txt") as f:           
    springs = list()
    for line in f.readlines():
        springs.append(["?".join([line.split()[0] for i in range(5)]), eval("["+",".join([line.split()[1] for i in range(5)])+"]")])
solutions = list()
for row, clues in springs:
    solutions.append(get_solutions(row,clues))
print(sum(solutions))
