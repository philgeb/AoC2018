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

def calc_rooms_path_at_least_1000(last_path_size, xy_offset):
    global rooms
    curr_x_off, curr_y_off = xy_offset
    curr = f.read(1)
    curr_path_size = last_path_size
    while curr != ")" and curr != "$":
        if curr == "|":
            curr_path_size = last_path_size
            curr_x_off, curr_y_off = xy_offset
        elif curr == "(":
            calc_rooms_path_at_least_1000(curr_path_size, (curr_x_off, curr_y_off))
        else:
            if curr == "N": curr_y_off += 1
            elif curr == "S": curr_y_off -= 1
            elif curr == "W": curr_x_off -= 1
            elif curr == "E": curr_x_off += 1

            curr_path_size += 1
            curr_pos = (curr_x_off, curr_y_off)
            if not curr_pos in visited_locations:
                if curr_path_size >= 1000:
                    rooms += 1
                visited_locations.add(curr_pos)

        curr = f.read(1)

def part1():
    print(calc_size_of_longest_alternative())

def part2():
    calc_rooms_path_at_least_1000(0, (0,0))
    print(rooms)

f = open("input20.txt", "r")

# ingore ^ char
f.read(1)

rooms = 0
visited_locations = set()

part2()
