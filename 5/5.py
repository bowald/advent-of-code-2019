def value(mode, pointer, memory):
    v = memory[pointer]
    if mode == '1':
        return v
    return memory[v]


def run_op(pc, memory):
    inst = str(memory[pc]).zfill(5)

    op = inst[-2:]
    modes = inst[:-2]
    
    if op == '01': # add
        a = value(modes[2], pc+1, memory)
        b = value(modes[1], pc+2, memory)
        addr = value('1', pc+3, memory)
        memory[addr] = a + b
        return pc + 4
    elif op == '02': # mul
        a = value(modes[2], pc+1, memory)
        b = value(modes[1], pc+2, memory)
        addr = value('1', pc+3, memory)
        memory[addr] = a * b
        return pc + 4
    elif op == '03': # stdin
        n = int(input('--> '))
        addr = value('1', pc+1, memory)
        memory[addr] = n
        return pc + 2
    elif op == '04': # stdout
        v = value(modes[2], pc+1, memory)
        print(v)
        return pc + 2
    elif op == '05': # jump-if-true
        a = value(modes[2], pc+1, memory)
        if a:
            return value(modes[1], pc+2, memory)
        return pc + 3
    elif op == '06': # jump-if-false
        a = value(modes[2], pc+1, memory)
        if a == 0:
            return value(modes[1], pc+2, memory)
        return pc + 3
    elif op == '07': # less than
        a = value(modes[2], pc+1, memory)
        b = value(modes[1], pc+2, memory)
        addr = value('1', pc+3, memory)
        memory[addr] = int(a < b)
        return pc + 4
    elif op == '08': # equals
        a = value(modes[2], pc+1, memory)
        b = value(modes[1], pc+2, memory)
        addr = value('1', pc+3, memory)
        memory[addr] = int(a == b)
        return pc + 4
    elif op == '99':
        return -1
    else:
        raise Exception(f'Unexcpected opcode: {op}, pc: {pc}')

def run(program):
    pc = 0
    while True:
        pc = run_op(pc, program)
        if pc < 0:
            break
        
input_data = [int(l) for l in open('input.txt').readline().split(',')]
run(input_data)


