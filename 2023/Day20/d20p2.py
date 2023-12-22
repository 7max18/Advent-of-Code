#In the puzzle input, each flip-flop either has another flip-flop 
#or a flip-flop and a conjunction as inputs.
#After sending a low signal, each conjunction sends said signal to at least one of its inputs, turning it off;
#This means the signal only lasts a moment between presses each time.
#There are four long chains of flip-flops, with each link connected to the same conjunction.
#Since flip-flops form chains, the period doubles between each.
#Hence, each quadrant can be represented as a large binary number.
#Each reset affects the root of the chain, effectively zeroing everyting.
#Find the number represented by the inputs of the four main conjunctions, followed by the lcm of those numbers.

from math import lcm

flip_flops = list()
conjunctions = list()

with open("Day20Input.txt") as f:
    for line in f.readlines():
        line = line.split()
        prefix = line[0][0]
        name = line[0][1:]
        destinations = [x.replace(",", "") for x in line[2:]]
        if prefix == "%":
            flip_flops.append((name, destinations))
        elif prefix == "&":
            conjunctions.append((name, destinations))
        else:
            broadcasted = destinations

chains = list()

for dest in broadcasted:
    module_chain = [dest]
    next_destinations = [x[1] for x in flip_flops if x[0] == dest][0]
    target_junction = [x for x in next_destinations if x in [c[0] for c in conjunctions]][0]
    next_flip_flop = [x for x in next_destinations if x != target_junction][0]
    module_chain.append(next_flip_flop)
    target_num_one = "1"
    while True:
        next_destinations = [x[1] for x in flip_flops if x[0] == next_flip_flop]
        next_destinations = next_destinations[0]
        if target_junction in next_destinations:
            target_num_one = "1" + target_num_one
        else:
            target_num_one = "0" + target_num_one
        next_flip_flop = [x for x in next_destinations if x != target_junction]
        if next_flip_flop:
            next_flip_flop = next_flip_flop[0]
            module_chain.append(next_flip_flop)
        else:
            break
    target_num_two = target_num_one
    #This confirms that everything zeros out.
    altered_bits = [x[1] for x in conjunctions if x[0] == target_junction][0]
    for bit in altered_bits:
        if bit not in [c[0] for c in conjunctions]:
            pos = module_chain[::-1].index(bit)
            while target_num_two[pos] == "1" and pos >= 0:
                target_num_two = target_num_two[:pos]+"0"+target_num_two[pos+1:]
                pos -= 1
            if pos >= 0:
                target_num_two = target_num_two[:pos]+"1"+target_num_two[pos+1:]
    chains.append((target_junction, int(target_num_one, 2), int(target_num_two, 2)))
print(lcm(*[n[1] for n in chains]))
        

