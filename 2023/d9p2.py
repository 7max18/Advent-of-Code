histories = list()

with open("Input/Day9Input.txt") as f:
    for line in f.readlines():
        histories.append([int(x) for x in line.split()])

backs = list()
for history in histories:
    diffs = history
    starts = [history[0]]
    while any(diffs):
        diffs = [v - diffs[i] for i,v in enumerate(diffs[1:])]
        starts.append(diffs[0])
    back = 0
    for index, start in enumerate(starts):
        if index % 2 == 0:
            back += start
        else:
            back -= start
    backs.append(back)
print(sum(backs))