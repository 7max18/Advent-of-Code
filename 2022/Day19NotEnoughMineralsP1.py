import sys
import re
import json
from copy import deepcopy
from collections import defaultdict

TOTAL_MINUTES = 24
class Blueprint:
    init_state = {"resources": {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0},
                  "robots": {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}}
    def __init__(self, values):
        self.id = int(values[0])
        self.costs = {
            "ore": {"ore": int(values[1]), "clay": 0, "obsidian": 0},
            "clay": {"ore": int(values[2]), "clay": 0, "obsidian": 0},
            "obsidian": {"ore": int(values[3]), "clay": int(values[4]), "obsidian": 0},
            "geode": {"ore": int(values[5]), "clay": 0, "obsidian": int(values[6])}
        }
        self.ranks = ["ore", "clay", "obsidian", "geode"]
        self.explored = set()
    def produce(self, minute, state = init_state):
        for robot_type, robots in list(state["robots"].items())[:-1]:
            most_needed = max([x[robot_type] for x in self.costs.values()])
            if robots > most_needed:
                return 0    
        if minute == TOTAL_MINUTES:
            geode_count = state["resources"]["geode"]
            #print(state)
            return geode_count
        cumulative_resources = sum(state["resources"].values())
        mapp = defaultdict(list)
        new = set()
        for resources, robots, total in self.explored:
            mapp[robots].append((resources, robots, total))
        for group in mapp.values():
            sgroup = set(group)
            for s in sorted(group, key=lambda x:x[2], reverse=True):
                if s not in sgroup:
                    continue
                sgroup = {x for x in sgroup if s == x or not all(v1 >= v2 for (v1, v2) in zip(s[0], x[0]))}
            new |= sgroup
        self.explored = new
        print(len(self.explored))
        self.explored.add((tuple(state["resources"].values()), tuple(state["robots"].values()), cumulative_resources))
        options = list()
        for robot in ["ore", "clay", "obsidian", "geode"]:
            for key, value in self.costs[robot].items():
                if state["resources"][key] < value:
                    break
            else:
                option = deepcopy(state)
                for key, value in self.costs[robot].items(): 
                    option["resources"][key] -= value
                for key, value in option["robots"].items():
                    option["resources"][key] += value
                option["robots"][robot] += 1
                options.append(option)
        wait_option = deepcopy(state)
        for key, value in wait_option["robots"].items():
            wait_option["resources"][key] += value
        options.append(wait_option)
        return max([self.produce(minute+1, option) for option in options])
            
file = sys.argv[1]

blueprints = list()

with open(f"./{file}") as f:
    for line in f:
        values = re.findall(r'\d+', line)
        blueprints.append(Blueprint(values))

quality = 0

for blueprint in [blueprints[0]]:
    print(blueprint.id, blueprint.produce(0))
