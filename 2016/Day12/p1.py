def reg_to_index(reg):
    return 'abcd'.index(reg)

with open('input.txt') as f:
    instructions = [[int(x) if not x.isalpha() else x for x in line.split()] for line in f.readlines()]

regs = [0,0,0,0]

pc = 0

while pc < len(instructions):
    ins = instructions[pc]
    opcode, operands = ins[0], ins[1:]
    match opcode:
        case 'cpy':
            dest = reg_to_index(operands[1])
            if type(operands[0]) is int:
                regs[dest] = operands[0]
            else:
                regs[dest] = regs[reg_to_index(operands[0])]
            pc += 1
        case 'inc':
            regs[reg_to_index(operands[0])] += 1
            pc += 1
        case 'dec':
            regs[reg_to_index(operands[0])] -= 1
            pc += 1
        case 'jnz':
            if type(operands[0]) is int:
                test = operands[0]
            else:
                test = regs[reg_to_index(operands[0])]
            if test != 0:
                pc += operands[1]
            else:
                pc += 1

print(regs[0])

