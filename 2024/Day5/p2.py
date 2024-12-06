#To move a page that goes before a page that it shoud follow, 
# it AND every page known to follow it
# needs to go immediately after the other page, assuming the rules contain no contradictions.
# The same applies to any page moved in the process, which should propagate as pages are moved forward.

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
    starting_correct = True
    tethers = {x: list() for x in update}
    for rule in relevant_rules:
        tethers[rule[1]].append(rule[0])
    for index, page in enumerate(update):
        for scanned in update[:index]:
            if page in tethers[scanned]:
                update.insert(index, update.pop(update.index(scanned)))
                starting_correct = False
    if not starting_correct:
        total += update[len(update)//2]

print(total)
