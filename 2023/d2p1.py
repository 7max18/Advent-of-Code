LIMITS = {"red":12, "green":13,"blue":14}

games = list()

with open("Input/Day2Input.txt") as f:
    for line in f.readlines():
        new_line = " ".join(line.split()[2::])
        new_line = [[y.split()[::-1] for y in x.split(", ")] for x in new_line.split("; ")]
        game = [{ k:int(v) for k, v in x} for x in new_line]
        games.append(game)

valid_ids = list()

for index, game in enumerate(games):
    for round in game:
        for color in round:
            if round[color] > LIMITS[color]:
                break
        else:
            continue
        break
    else:
        valid_ids.append(index+1)

print(sum(valid_ids))