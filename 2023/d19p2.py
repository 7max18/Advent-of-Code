class Part():
    def __init__(self, x, m, a, s):
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
        accepted = 0
        cur_part = part
        for rule in self.rules[:-1]:
            rating, condition, boundary = rule[0][0], rule[0][1], int(rule[0][2:])
            cur_rating = eval("cur_part."+rating)
            if condition == "<":
                passed, failed = (cur_rating[0], min(cur_rating[1], boundary)), (max(cur_rating[0], boundary), cur_rating[1])
            else:
                passed, failed = (max(cur_rating[0], boundary+1), cur_rating[1]), (cur_rating[0], min(cur_rating[1], boundary+1))
            if passed[1] <= passed[0]:
                passed = (0,0)
            if failed[1] <= failed[0]:
                failed = (0,0)
            match rating:
                case "x":
                    passed, failed = Part(passed, cur_part.m, cur_part.a, cur_part.s), Part(failed, cur_part.m, cur_part.a, cur_part.s)
                case "m":
                    passed, failed = Part(cur_part.x, passed, cur_part.a, cur_part.s), Part(cur_part.x, failed, cur_part.a, cur_part.s)
                case "a":
                    passed, failed = Part(cur_part.x, cur_part.m, passed, cur_part.s), Part(cur_part.x, cur_part.m, failed, cur_part.s)
                case "s":
                    passed, failed = Part(cur_part.x, cur_part.m, cur_part.a, passed), Part(cur_part.x, cur_part.m, cur_part.a, failed)
            cur_part = failed
            if rule[1] == "A":
                accepted += (passed.x[1]-passed.x[0]) * (passed.m[1]-passed.m[0]) * (passed.a[1]-passed.a[0]) * (passed.s[1]-passed.s[0])
            elif rule[1] == "R":
                continue
            elif eval("passed."+rating+"!=(0,0)"):
                accepted += rule[1].consider(passed)
        if self.rules[-1] == "A" and eval("cur_part."+rating+"!=(0,0)"):
            accepted += (cur_part.x[1]-cur_part.x[0]) * (cur_part.m[1]-cur_part.m[0]) * (cur_part.a[1]-cur_part.a[0]) * (cur_part.s[1]-cur_part.s[0])
        elif self.rules[-1] != "R":
            accepted += self.rules[-1].consider(cur_part)
        return accepted
            
workflows = list()
accepted = list()

with open("Input/Day19Input.txt") as f:
    lines = f.readlines()
    at_parts = False
    for line in lines:
        if line.strip():
            name, rules = line.strip()[:-1].split("{")
            rules = [rule.split(":") for rule in rules.split(",")[:-1]] + [rules.split(",")[-1]]
            workflows.append(Workflow(name, rules))
        else:
            break

for workflow in workflows:
    workflow.get_connections()
start = [workflow for workflow in workflows if workflow.name == "in"][0]
print(start.consider(Part((1,4001),(1,4001),(1,4001),(1,4001))))
