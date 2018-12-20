def calc_size_of_longest_alternative():
    curr = f.read(1)
    sub_path_sums = [0]
    while curr != ")" and curr != "$":
        if curr == "|":
            sub_path_sums.append(0)
        elif curr == "(":
            sub_path_sums[-1] += calc_size_of_longest_alternative()
        else:
            sub_path_sums[-1] += 1
        curr = f.read(1)

    # detour
    if sub_path_sums[-1] == 0:
        return 0

    return max(sub_path_sums)

detour_indicator = ["NS", "SN", "WE", "EW"]

def calc_rooms_path_at_least_1000(last_path_size):
    global rooms
    curr = f.read(1)
    curr_path_size = last_path_size
    while curr != ")" and curr != "$":
        if curr == "|":
            curr_path_size = last_path_size
        elif curr == "(":
            calc_rooms_path_at_least_1000(curr_path_size)
        else:
            curr_path_size += 1
            # strict greater than because number of passed doors = curr_path_size + 1
            if curr_path_size > 10:
                rooms += 1

        prev = curr
        curr = f.read(1)

        # ignore the backtracking part of detours
        if prev + curr in detour_indicator:
            while(curr != "|"):
                curr = f.read(1)

def part1():
    print(calc_size_of_longest_alternative())

def part2():
    calc_rooms_path_at_least_1000(0)
    print(rooms)

f = open("input20.txt", "r")

# ingore ^ char
f.read(1)

rooms = 0

part2()
