import re

# this is basically a really slow algorithm to calculate the sum of all divisors of a number (incl. itself)
# after the first couple instructions the number is stored in register 4
# for part 2 this number is too big to run on this algorithm in an acceptable time, so instead use a faster version:
def faster_alg(number):
    sum_divs = 0
    for i in range(1, number + 1):
        if number % i == 0:
            sum_divs += i
    print(sum_divs)

def addr(state, a, b, c):
    state[c] = state[a] + state[b]

def addi(state, a, b, c):
    state[c] = state[a] + b

def mulr(state, a, b, c):
    state[c] = state[a] * state[b]

def muli(state, a, b, c):
    state[c] = state[a] * b

def banr(state, a, b, c):
    state[c] = state[a] & state[b]

def bani(state, a, b, c):
    state[c] = state[a] & b

def borr(state, a, b, c):
    state[c] = state[a] | state[b]

def bori(state, a, b, c):
    state[c] = state[a] | b

def setr(state, a, b, c):
    state[c] = state[a]

def seti(state, a, b, c):
    state[c] = a

def gtir(state, a, b, c):
    state[c] = 1 if a > state[b] else 0

def gtri(state, a, b, c):
    state[c] = 1 if state[a] > b else 0

def gtrr(state, a, b, c):
    state[c] = 1 if state[a] > state[b] else 0

def eqir(state, a, b, c):
    state[c] = 1 if a == state[b] else 0

def eqri(state, a, b, c):
    state[c] = 1 if state[a] == b else 0

def eqrr(state, a, b, c):
    state[c] = 1 if state[a] == state[b] else 0

f = open("input19.txt", "r")

instr_reg = int(f.readline()[4])

instructions = []

for l in f.readlines():
    op = locals()[l[:4]]
    a, b, c = list(map(int, re.findall(r'\d+', l)))
    instructions.append((op, a, b, c))

state = [0,0,0,0,0,0]
instr_index = 0

while instr_index < len(instructions):
    op, a, b, c = instructions[instr_index]
    op(state, a, b, c)
    state[instr_reg] += 1
    instr_index = state[instr_reg]

print(state[0])