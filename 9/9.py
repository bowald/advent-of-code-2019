import os

class InputInteruption(Exception):
    """Raised when intComputer wants an input"""
    def __init__(self, pc):
        self.pc = pc

# class OutputInteruption(Exception):
#     """Raised when intComputer gives an output"""
#     def __init__(self, pc):
#         self.pc = pc

class IntComputer:
    def __init__(self, program):
        self.pc = 0
        self.memory = program + [0] * (4096 - len(program))
        self.relative_base = 0
        self.input_reg = []
        self.output_reg = []

    def run(self):
        while True:
            self.pc = self.run_op(self.pc)
            if self.pc < 0:
                break
        
    def run_op(self, pc):
        inst = str(self.memory[pc]).zfill(5)

        op = inst[-2:]
        modes = inst[:-2]
        
        if op == '01': # add
            a = self.value(modes[2], pc+1)
            b = self.value(modes[1], pc+2)
            addr = self.memory[pc+3]
            self.write(modes[0], addr, a + b)
            return pc + 4
        elif op == '02': # mul
            a = self.value(modes[2], pc+1)
            b = self.value(modes[1], pc+2)
            addr = self.memory[pc+3]
            self.write(modes[0], addr, a * b)
            return pc + 4
        elif op == '03': # stdin
            if len(self.input_reg) < 1:
                raise InputInteruption(pc)
            n = self.input_reg.pop()
            addr = self.memory[pc+1]
            self.write(modes[2], addr, n)
            return pc + 2
        elif op == '04': # stdout
            v = self.value(modes[2], pc+1)
            print(v)
            self.output_reg.append(v)
            # raise OutputInteruption(pc + 2)
            return pc + 2
        elif op == '05': # jump-if-true
            a = self.value(modes[2], pc+1)
            if a:
                return self.value(modes[1], pc+2)
            return pc + 3
        elif op == '06': # jump-if-false
            a = self.value(modes[2], pc+1)
            if a == 0:
                return self.value(modes[1], pc+2)
            return pc + 3
        elif op == '07': # less than
            a = self.value(modes[2], pc+1)
            b = self.value(modes[1], pc+2)
            addr = self.memory[pc+3]
            self.write(modes[0], addr, int(a < b))
            return pc + 4
        elif op == '08': # equals
            a = self.value(modes[2], pc+1)
            b = self.value(modes[1], pc+2)
            addr = self.memory[pc+3]
            self.write(modes[0], addr, int(a == b))
            return pc + 4
        elif op == '09': # relative base offfset
            self.relative_base += self.value(modes[2], pc+1)
            return pc + 2
        elif op == '99':
            return -1
        else:
            raise Exception(f'Unexcpected opcode: {op}, pc: {pc}')
        
    def value(self, mode, pointer):
        v = self.memory[pointer]
        if mode == '1':
            return v
        elif mode == '2':
            return self.memory[self.relative_base + v]
        return self.memory[v]

    def write(self, mode, addr, value):
        if mode == '2':
            self.memory[self.relative_base + addr] = value
        else:
            self.memory[addr] = value


# Driver program to test above function 
program = [int(l) for l in open(os.path.join(os.path.dirname(__file__),'input.txt')).readline().split(',')]
c = IntComputer(program)
# c.input_reg.append(1)
c.input_reg.append(2)
c.run()
