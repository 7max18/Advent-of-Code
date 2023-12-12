scratchcards = list()

with open("Input/Day4Input.txt") as f:
    for line in f.readlines():
        winning_numbers = list()
        numbers_you_have = list()
        numbers = line.split()[2:]
        reached_split = False
        for number in numbers:
            if number == "|":
                reached_split = True
            elif reached_split:
                numbers_you_have.append(int(number))
            else:
                winning_numbers.append(int(number))
        scratchcards.append([winning_numbers, numbers_you_have])

total = list()

for card in scratchcards:
    points = 0
    for number in card[1]:
        if number in card[0]:
            if points == 0:
                points = 1
            else:
                points *= 2
    total.append(points)

print(sum(total))
