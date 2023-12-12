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
        scratchcards.append([winning_numbers, numbers_you_have, 1])

for i, card in enumerate(scratchcards):
    wins = 0
    for number in card[1]:
        if number in card[0]:
            wins+=1
    for j in range(i+1, i+wins+1):
        scratchcards[j][2] += card[2]
print(sum([card[2] for card in scratchcards]))
