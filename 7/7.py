class InputInteruption(Exception):
    """Raised when intComputer wants an input"""
    def __init__(self, pc):
        self.pc = pc

class OutputInteruption(Exception):
    """Raised when intComputer gives an output"""
    def __init__(self, pc):
        self.pc = pc

class IntComputer:
    def __init__(self, program):
        self.pc = 0
        self.memory = program.copy()
        
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
            addr = self.value('1', pc+3)
            self.memory[addr] = a + b
            # print(f'ADD {a} + {b} = {a + b} store at: {addr}')
            return pc + 4
        elif op == '02': # mul
            a = self.value(modes[2], pc+1)
            b = self.value(modes[1], pc+2)
            addr = self.value('1', pc+3)
            self.memory[addr] = a * b
            # print(f'MUL {a} * {b} = {a * b} store at: {addr}')
            return pc + 4
        elif op == '03': # stdin
            if len(self.input_reg) < 1:
                raise InputInteruption(pc)
            n = self.input_reg.pop()
            addr = self.value('1', pc+1)
            self.memory[addr] = n
            return pc + 2
        elif op == '04': # stdout
            v = self.value(modes[2], pc+1)
            self.output_reg.append(v)
            raise OutputInteruption(pc + 2)
            # return pc + 2
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
            addr = self.value('1', pc+3)
            self.memory[addr] = int(a < b)
            return pc + 4
        elif op == '08': # equals
            a = self.value(modes[2], pc+1)
            b = self.value(modes[1], pc+2)
            addr = self.value('1', pc+3)
            self.memory[addr] = int(a == b)
            return pc + 4
        elif op == '99':
            return -1
        else:
            raise Exception(f'Unexcpected opcode: {op}, pc: {pc}')
        
    def value(self, mode, pointer):
        v = self.memory[pointer]
        if mode == '1':
            return v
        return self.memory[v]


def permutation(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 
  

# Driver program to test above function 
# possible_settings = permutation(list('01234'))
possible_settings = permutation(list('56789'))
best_setting = []
maximun_thrust = -1

# input_data = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# input_data = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
# input_data = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
# input_data = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
# input_data = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
input_data = [3,8,1001,8,10,8,105,1,0,0,21,46,55,72,85,110,191,272,353,434,99999,3,9,1002,9,5,9,1001,9,2,9,102,3,9,9,101,2,9,9,102,4,9,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,101,2,9,9,1002,9,2,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,4,9,99,3,9,1002,9,3,9,101,5,9,9,1002,9,3,9,101,3,9,9,1002,9,5,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99]
# input_data = [int(l) for l in open('input.txt').readline().split(',')]

for phase_setting in possible_settings:
    # last_input = 0
    # run the amplifiers
    amplifiers = []
    for i in range(5):
        c = IntComputer(input_data)
        
        # Amplifier A starts with input 0
        if (i < 1):
            c.input_reg.append(0)
        
        # Set phase
        c.input_reg.append(int(phase_setting[i]))
        amplifiers.append(c)

    running = 0
    while True:
        c = amplifiers[running]
        try:
            c.run()
            running += 1
            if running > 4:
                break
        except InputInteruption as e:
            # nextC = (running - 1) % 5
            print('hopefully this will no happen')
        except OutputInteruption as e:
            c.pc = e.pc # Make amplifier move to next instruction
            nextC = (running + 1) % 5
            output = c.output_reg.pop()
            amplifiers[nextC].input_reg.insert(0, output)
            last_input = (output, running)
            running = nextC
        except Exception as e:
            print(phase_setting)
            print(last_input)
            break

    if last_input[0] > maximun_thrust:
        maximun_thrust = last_input[0]
        best_setting = phase_setting

print(f'maximum thrust {maximun_thrust} when using setting: {"".join(best_setting)}')