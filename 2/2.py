def run_op(op, i0, i1, res, memory):
    if op == 1:
        memory[res] = memory[i0] + memory[i1]
        return True
    elif op == 2:
        memory[res] = memory[i0] * memory[i1]
        return True
    elif op == 99:
        return False
    else:
        return False

def run(program):
    c = 0
    running = True
    while running:
        running = run_op(program[c], program[c + 1], program[c + 2], program[c + 3], program)
        c += 4

    return program[0]

input_data = [int(l) for l in open('input.txt').readline().split(',')]

# Part 1
# input_data[1] = 12
# input_data[2] = 2
# print(run(input_data))

# Part 2
for noun in range(100):
    input_data[1] = noun
    for verb in range(100):
        input_data[2] = verb

        result = run(input_data.copy())
        if result == 19690720:
            print(100 * noun + verb)
            quit()


