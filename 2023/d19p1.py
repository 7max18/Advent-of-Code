class Part():
    def __init__(self, x, m, a ,s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

class Workflow():
    def __init__(self, name, rules):
        self.name = name
        self.rules = rules
    def get_connections(self):
        last = self.rules[-1]
        self.rules = [[rule[0], rule[1]] if rule[1] in "AR" else [rule[0],[workflow for workflow in workflows if workflow.name == rule[1]][0]] for rule in self.rules[:-1]]
        if last == "A" or last == "R":
            self.rules.append(last)
        else:
            self.rules += [workflow for workflow in workflows if workflow.name == last]
    def consider(self, part:Part):
        for rule in self.rules[:-1]:
            if eval("part." + rule[0]):
                if rule[1] == "A":
                    return True
                elif rule[1] == "R":
                    return False
                else:
                    return rule[1].consider(part)
        else:
            if self.rules[-1] == "A":
                return True
            elif self.rules[-1] == "R":
                return False
            else:
                return self.rules[-1].consider(part)

        
workflows = list()
parts = list()
accepted = list()

with open("Input/Day19Input.txt") as f:
    lines = f.readlines()
    at_parts = False
    for line in lines:
        if line.strip():
            if at_parts:
                part_ratings = line.strip()[1:-1].split(",")
                parts.append(Part(int(part_ratings[0][2:]), int(part_ratings[1][2:]), int(part_ratings[2][2:]), int(part_ratings[3][2:])))
            else:
                name, rules = line.strip()[:-1].split("{")
                rules = [rule.split(":") for rule in rules.split(",")[:-1]] + [rules.split(",")[-1]]
                workflows.append(Workflow(name, rules))
        else:
            at_parts = True

for workflow in workflows:
    workflow.get_connections()

start = [workflow for workflow in workflows if workflow.name == "in"][0]
for part in parts:
    if start.consider(part):
        accepted.append(part)

total_ratings = 0
for part in accepted:
    total_ratings += part.x + part.m + part.a + part.s

print(total_ratings)
