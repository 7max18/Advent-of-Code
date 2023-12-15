#What's more efficient? To sweep from the top down or bottom up?
#Top down: 2n time.

with open("Input/Day14Input.txt") as f:
    platform = [line.strip() for line in f.readlines()]

for i in range(1, len(platform)):
    for j in range(i, 0, -1):
        for k in range(len(platform[0])):
            if platform[j][k] == "O":
                if platform[j-1][k] == ".":
                    platform[j] = platform[j][:k]+"."+platform[j][k+1:]
                    platform[j-1] = platform[j-1][:k]+"O"+platform[j-1][k+1:]
load = 0
for index, row in enumerate(platform[::-1]):
    load += (index+1) * row.count("O")
print(load)