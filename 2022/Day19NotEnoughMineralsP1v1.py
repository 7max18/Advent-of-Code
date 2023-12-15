import sys
import re
import numpy as np

TOTAL_MINUTES = 24

class Blueprint:
    def __init__(self, values):
        self.id = int(values[0])
        self.costs = {
            "ore": {"ore": int(values[1]), "clay": 0, "obsidian": 0},
            "clay": {"ore": int(values[2]), "clay": 0, "obsidian": 0},
            "obsidian": {"ore": int(values[3]), "clay": int(values[4]), "obsidian": 0},
            "geode": {"ore": int(values[5]), "clay": 0, "obsidian": int(values[6])}
        }
        self.resources = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
        self.robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
        self.ranks = ["ore", "clay", "obsidian", "geode"]
    #Cookie clicker formula: cost / current CPS + cost / delta CPS
    def cost_rating(self, robot_type):
        rating = float(0)
        for resource in self.costs[robot_type]:
            if self.robots[robot_type]:
                rating += self.costs[robot_type][resource] / self.robots[robot_type]
            rating += self.costs[robot_type][resource]
        return rating, robot_type
    def wait_rating(self, robot_type):
        wait_times = list()
        for resource in [ x for x in self.costs[robot_type] if self.costs[robot_type][x] > 0]:
            if self.robots[resource]:
                wait_times.append([resource, max([0, self.costs[robot_type][resource] - self.resources[resource]]) // self.robots[resource]])
            else:
                wait_times.append([resource, -1])
        time = max(wait_times, key=lambda x: x[1])
        rating = self.cost_rating(robot_type)
        # if self.robots[robot_type]:
        #     rating += self.costs[robot_type][time[0]] / self.robots[robot_type]
        # if time[1] > 0:
        #     if self.robots[robot_type]:
        #         rating += self.costs[robot_type][time[0]] / (self.robots[robot_type] * (time[1]))
        #     else:
        #         rating += self.costs[robot_type][time[0]] / (self.robots[robot_type] * (time[1]))
        return rating, time[1]
    # def wait_rating(self, robot_type):
    #     rating = float(0)
    #     for resource in self.costs[robot_type]:
    #         if self.robots[robot_type]:
    #             rating += self.costs[robot_type][resource] / self.robots[robot_type] + self.costs[robot_type][resource] / self.robots[robot_type] * 2
    #     return rating
    #In each minute, the following happens in order: Spend ore, collect ore, build robots.
    def produce(self):
        for minute in range(TOTAL_MINUTES):
            options = list()
            build = None
            for robot in self.robots.keys():
                for key, value in self.costs[robot].items():
                    if self.resources[key] < value:
                        break
                else:
                    options.append(robot)
            # print(options)
            # print(self.robots)
            # print(self.resources)
            if options:
                #build = max([self.cost_rating(x) for x in options])[1]
                if options[-1] == self.ranks[-1]:
                    build = options[-1]
                else:
                    cur_rankings = list()
                    delta_rankings = list()
                    time_rankings = list()
                    for option in self.ranks:
                        
                        if option == "ore":
                            cur = max(0, int(np.ceil((self.costs["ore"]["ore"]+1)-self.resources["ore"]/2**(self.robots["ore"]-1))-self.resources["ore"]))
                            delta = np.inf
                            continue
                        if self.robots[self.ranks[self.ranks.index(option)-1]]:
                            cur = max(0, int(np.ceil((self.costs[option][self.ranks[self.ranks.index(option)-1]]-self.resources[self.ranks[self.ranks.index(option)-1]])/self.robots[self.ranks[self.ranks.index(option)-1]])))
                        else:
                            cur = np.inf
                        if self.robots[option]:
                            delta = int(np.ceil((np.ceil((self.costs[self.ranks[self.ranks.index(option)+1]][option]-(self.resources[option]))/(self.robots[option])))-(self.costs[self.ranks[self.ranks.index(option)+1]][option]-(self.robots[option]+1+self.resources[option]))/(self.robots[option]+1)))
                        else:
                            delta = np.inf
                        time_rankings.append((cur, self.ranks.index(option), delta))
                    # for option in self.ranks[:-1]:
                    #     if self.robots[option]:
                    #         cur_wait = (self.costs[self.ranks[self.ranks.index(option)+1]][option] - self.resources[option] + self.robots[option]) // self.robots[option]
                    #     else:
                    #         cur_wait = 999
                    #     improved_wait = (self.costs[self.ranks[self.ranks.index(option)+1]][option] - self.robots[option]) // (self.robots[option] + 1)
                    #     rankings.append((option, cur_wait))
                    time_rankings.sort(key=lambda x: (x[1]))
                    print(time_rankings)
                    print(options)
                    # choices = [r for r in time_rankings if self.ranks[r[1]] in options]
                    # choices.sort()
                    for index, rank in enumerate(time_rankings[:-1]):
                        # if index == 0:
                        #     if rank[0] <= time_rankings[index+1][0]:
                        #         best = rank
                        #         break
                        if rank[2] < time_rankings[index+1][0]:
                            best = rank
                            break
                    else:
                        best = time_rankings[-1]
                    if self.ranks[best[1]] in options:
                        build = self.ranks[best[1]]
                            
            if build:
                for key, value in self.costs[build].items(): 
                    self.resources[key] -= value
            for key, value in self.robots.items():
                self.resources[key] += value
            if build:
                print(f"{minute + 1}. {build}")
                self.robots[build] += 1
            else:
                print(f"{minute + 1}. wait")
        return self.resources["geode"]
            

file = sys.argv[1]

blueprints = list()

with open(f"./{file}") as f:
    for line in f:
        values = re.findall(r'\d+', line)
        blueprints.append(Blueprint(values))

quality = 0

for blueprint in blueprints:
    print(blueprint.id, blueprint.produce())

#Nothing increases ore production aside from building ore robots.