class Module:
    def get_destinations(self):
        dest_modules = list()
        for dest in self.destinations:
            if dest in [module.name for module in modules]:
                dest_modules.append([module for module in modules if module.name == dest][0])
            else:
                dest_modules.append(dest)
        self.destinations = dest_modules
        for module in self.destinations:
            if type(module) == Conjunction:
                module.memory[self.name] = False

class Broadcaster(Module):
    def __init__(self, destinations):
        self.name = "broadcaster"
        self.destinations = destinations
    def pulse(self, src_pulse, src_name):
        for dest in self.destinations:
            pulse_queue.append((self.name, src_pulse, dest))

class FlipFlop(Module):
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations
        self.on = False
    def pulse(self, src_pulse, src_name):
        if src_pulse == False:
            self.on = not self.on
            for dest in self.destinations:
                pulse_queue.append((self.name, self.on, dest))

class Conjunction(Module):
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations
        self.memory = dict()
    def pulse(self, src_pulse, src_name):
        self.memory[src_name] = src_pulse
        if all(self.memory.values()):
            for dest in self.destinations:
                pulse_queue.append((self.name, False, dest))
        else:
            for dest in self.destinations:
                pulse_queue.append((self.name, True, dest))

modules = list()

with open("Day20Input.txt") as f:
    for line in f.readlines():
        line = line.split()
        prefix = line[0][0]
        name = line[0][1:]
        destinations = [x.replace(",", "") for x in line[2:]]
        if prefix == "%":
            modules.append(FlipFlop(name, destinations))
        elif prefix == "&":
            modules.append(Conjunction(name, destinations))
        else:
            broadcaster = Broadcaster(destinations)

broadcaster.get_destinations()

for module in modules:
    module.get_destinations()

low_pulses = 0
high_pulses = 0
pulse_queue = list()

for press in range(1000):
    pulse_queue.append(("button", False, broadcaster))
    while pulse_queue:
        #print([(next_pulse[0], next_pulse[1], next_pulse[2].name) for next_pulse in pulse_queue])
        next_pulse = pulse_queue.pop(0)
        if next_pulse[1]:
            high_pulses += 1
        else:
            low_pulses += 1
        if type(next_pulse[2]) != str:
            next_pulse[2].pulse(next_pulse[1], next_pulse[0])
    
print(low_pulses*high_pulses)

