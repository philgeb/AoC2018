import bisect
import string

f = open("input7.txt", "r")

constraints = [] # contains touples, e.g. (C, A) means C must be finished before A
for l in f.read().splitlines():
    constraints.append((l[5],l[36]))

def part1():
    remaining_tasks = [c for c in string.ascii_uppercase]
    ready_tasks = []
    done_tasks = []

    while remaining_tasks or ready_tasks:
        for char in remaining_tasks:
            ready = True
            for co in constraints:
                if char == co[1]:
                    ready = False
            if ready:
                bisect.insort(ready_tasks, char)

        remaining_tasks = list(filter(lambda task: task not in ready_tasks, remaining_tasks))
        chosen_task = ready_tasks[0]
        ready_tasks.remove(chosen_task)
        done_tasks.append(chosen_task)
        constraints = list(filter(lambda co: co[0] != chosen_task, constraints))

    print(''.join(done_tasks))

def update_lists(remaining_tasks, ready_tasks):
    for char in remaining_tasks:
        ready = True
        for co in constraints:
            if char == co[1]:
                ready = False
        if ready:
            bisect.insort(ready_tasks, char)

        remaining_tasks = list(filter(lambda task: task not in ready_tasks, remaining_tasks))

    return (remaining_tasks, ready_tasks)

def part2():
    i = 0 # time steps

    remaining_tasks = [c for c in string.ascii_uppercase]
    ready_tasks = ['G', 'J'] # hardcoded initally-ready tasks that we know from part1
    done_tasks = []
    workers = [] # touple of task and time left, e.g. (F, 23)

    while remaining_tasks or ready_tasks:
        i += 1

        for w in workers:
            if w[1] == 0:
                constraints = list(filter(lambda co: co[0] != w[0], constraints))
                remaining_tasks,ready_tasks = update_lists(remaining_tasks, ready_tasks)
                
            w[1] -= 1 # can get negative, so 0-condition is not true twice for the same task



part2()