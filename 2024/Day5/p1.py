rules = list()
updates = list()

with open('input.txt') as f:
      at_gap = False
      for line in f.readlines():
            if line == '\n':
                at_gap = True
            elif not at_gap:
                rules.append(tuple([int(x) for x in line.strip().split('|')]))
            else: 
                updates.append([int(x) for x in line.strip().split(',')])

total = 0

for update in updates:
    relevant_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
    for rule in relevant_rules:
        if update.index(rule[0]) > update.index(rule[1]):
            break
    else:
        total += update[len(update)//2]

print(total)

        