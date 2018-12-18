import bisect
import string

f = open("input7.txt", "r")

constraints = [] # contains touples, e.g. (C, A) means C must be finished before A
for l in f.read().splitlines():
    constraints.append((l[5],l[36]))

def part1():
    global constraints
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

class Worker:
    def __init__(self, task, remaining_time):
        self.task = task
        self.remaining_time = remaining_time

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
    global constraints

    remaining_tasks = [c for c in string.ascii_uppercase]
    ready_tasks = ['G', 'J'] # initially-ready tasks that we know from part 1
    workers = []

    i = 0 # time steps
    while constraints or workers:
        for w in workers:
            w.remaining_time -= 1
            if w.remaining_time == 0:
                constraints = list(filter(lambda co: co[0] != w.task, constraints))
                remaining_tasks, ready_tasks = update_lists(remaining_tasks, ready_tasks)
            
        workers = list(filter(lambda w: w.remaining_time > 0, workers))
        
        while len(workers) < 5 and ready_tasks:
            next_task_to_assign = ready_tasks.pop(0)
            workers.append(Worker(next_task_to_assign, 60 + ord(next_task_to_assign) - 64))

        i += 1

    print(i - 1) # counted one step too much apparently

part2()