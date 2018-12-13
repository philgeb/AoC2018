def part1():
    f = open("input12.txt", "r")

    l = f.readline()[:-1]
    state = "...." + l[15:] + "...."
    plant_0_index = 0

    # ignore empty line
    f.readline()

    rules = set() # only contains rules that result in "#""
    for l in f.read().splitlines():
        rule = l.split(" => ")
        if rule[1] == "#":
            rules.add((rule[0]))

    for _ in range(20):
        next_state = ".."
        for i in range(2, len(state) - 3):
            curr = state[i-2:i+3]
            if curr in rules:
                next_state += "#"
            else:
                next_state += "."

        first_plant_index = next_state.find("#")
        last_plant_index = next_state.rfind("#")
        state = "...." + next_state[first_plant_index:last_plant_index + 1] + "...."

        # keep track of 0-index
        plant_0_index += 4 - first_plant_index

    sum = 0
    stripped_state = state.lstrip(".")
    for i in range(len(stripped_state)):
        if stripped_state[i] == "#":
            sum += i - plant_0_index

    print(sum)

def part2():
    print(695 + 50 * 50000000000)

part1()