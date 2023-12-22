games = list()

with open("Day2Input.txt") as f:
    for line in f.readlines():
        new_line = " ".join(line.split()[2::])
        new_line = [[y.split()[::-1] for y in x.split(", ")] for x in new_line.split("; ")]
        game = [{ k:int(v) for k, v in x} for x in new_line]
        games.append(game)

powers = list()

for index, game in enumerate(games):
    fewest = {"red":0, "green":0, "blue":0}
    for round in game:
        for color in round:
            if round[color] > fewest[color]:
                fewest[color] = round[color]
    powers.append(fewest["red"] * fewest["green"] * fewest["blue"])
    
print(sum(powers))