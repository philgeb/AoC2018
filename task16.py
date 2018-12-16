import re

def addr(state, a, b, c):
    new_state = list(state)
    new_state[c] = state[a] + state[b]
    return new_state

def addi(state, a, b, c):
    new_state = list(state)
    new_state[c] = state[a] + b
    return new_state

def mulr(state, a, b, c):
    new_state = list(state)
    new_state[c] = state[a] * state[b]
    return new_state

def muli(state, a, b, c):
    new_state = list(state)
    new_state[c] = state[a] * b
    return new_state

def banr(state, a, b, c):
    new_state = list(state)
    new_state[c] = state[a] & state[b]
    return new_state

def bani(state, a, b, c):
    new_state = list(state)
    new_state[c] = state[a] & b
    return new_state

def borr(state, a, b, c):
    new_state = list(state)
    new_state[c] = state[a] | state[b]
    return new_state

def bori(state, a, b, c):
    new_state = list(state)
    new_state[c] = state[a] | b
    return new_state

def setr(state, a, b, c):
    new_state = list(state)
    new_state[c] = state[a]
    return new_state

def seti(state, a, b, c):
    new_state = list(state)
    new_state[c] = a
    return new_state

def gtir(state, a, b, c):
    new_state = list(state)
    new_state[c] = 1 if a > state[b] else 0
    return new_state

def gtri(state, a, b, c):
    new_state = list(state)
    new_state[c] = 1 if state[a] > b else 0
    return new_state

def gtrr(state, a, b, c):
    new_state = list(state)
    new_state[c] = 1 if state[a] > state[b] else 0
    return new_state

def eqir(state, a, b, c):
    new_state = list(state)
    new_state[c] = 1 if a == state[b] else 0
    return new_state

def eqri(state, a, b, c):
    new_state = list(state)
    new_state[c] = 1 if state[a] == b else 0
    return new_state

def eqrr(state, a, b, c):
    new_state = list(state)
    new_state[c] = 1 if state[a] == state[b] else 0
    return new_state

functions = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
opcode_to_possible_funcs = {}

samples_behaving_like_3_or_more_opcodes = 0

inp = open("input16.txt", "r")
curr = inp.readline()
while(not curr.isspace()):
    state = list(map(int, re.findall(r"\d+", curr)))
    op, a, b, c = map(int, re.findall(r"\d+", inp.readline()))
    new_state = list(map(int, re.findall(r"\d+", inp.readline())))

    matching_funcs = set()
    for f in functions:
        if f(state, a, b, c) == new_state:
            matching_funcs.add(f)

    if op not in opcode_to_possible_funcs:
        opcode_to_possible_funcs[op] = matching_funcs
    else:
        opcode_to_possible_funcs[op] = opcode_to_possible_funcs[op].intersection(matching_funcs)

    if len(matching_funcs) >= 3:
        samples_behaving_like_3_or_more_opcodes += 1

    inp.readline() # skip empty line
    curr = inp.readline()

# find exact opcode to function mappings
opcode_to_exact_func = {}
while(functions != []):
    for op in opcode_to_possible_funcs.keys():
        funcs = opcode_to_possible_funcs[op]
        if len(funcs) == 1: # op can be mapped to exactly one function
            func = next(iter(funcs)) # get the single member of the set

            # remove func from all opcode_to_possible_funcs mappings
            for op2 in opcode_to_possible_funcs.keys():
                opcode_to_possible_funcs[op2].discard(func)
 
            functions.remove(func)
            opcode_to_exact_func[op] = func

# run test program
test_program_state = [0, 0, 0, 0]

inp.readline()
for line in inp.readlines():
    op, a, b, c = map(int, re.findall(r"\d+", line))
    test_program_state = opcode_to_exact_func[op](test_program_state, a, b, c)

print(samples_behaving_like_3_or_more_opcodes) # part1
print(test_program_state[0]) # part2
