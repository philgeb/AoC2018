import re

f = open("input17.txt", "r")

# assumption: 400 < x < 610 and 0 < y < 2000
ground_matrix = [['.' for _ in range(220)] for _ in range (2000)]

# init values
ground_matrix[0][100] = '+'
init_x = 100
init_y = 1

for l in f.read().splitlines():
    nums = list(map(int, re.findall(r"\d+", l)))
    if l[0] == 'x':
        x = nums[0] - 400
        for y in range(nums[1], nums[2] + 1):
            ground_matrix[y][x] = '#'
    else:
        y = nums[0]
        for x in range(nums[1], nums[2] + 1):
            ground_matrix[y][x - 400] = '#'

def drop_to_next_clay_or_water(x, y):
    # terminate if right side overflow is already filled up because of left side overflow
    if ground_matrix[y][x] == '~':
        return

    while True:
        ground_matrix[y][x] = '|'

        # terminate if another water path already reached here or we reach the y limit
        if ground_matrix[y + 1][x] == '|' or y >= 1897:
            return
        # hit clay or still water, now fill up
        elif ground_matrix[y + 1][x] == '#' or ground_matrix[y + 1][x] == '~':
            fill_until_overflow(x, y)
            return

        y += 1

def find_left_wall_or_new_drop(x, y):
    while True:
        if ground_matrix[y + 1][x] == '.':
            return (x, False) # new drop
        elif ground_matrix[y][x - 1] == '#':
            return (x, True) # hit left wall
        x -= 1

def find_right_wall_or_new_drop(x, y):
    while True:
        if ground_matrix[y + 1][x] == '.':
            return (x, False) # new drop
        elif ground_matrix[y][x + 1] == '#':
            return (x, True) # hit left wall
        x += 1

def fill_until_overflow(x, y):
    while True:
        left_x, hit_left_wall = find_left_wall_or_new_drop(x, y)
        right_x, hit_right_wall = find_right_wall_or_new_drop(x, y)
        
        if not hit_left_wall or not hit_right_wall:
            break
        
        for ix in range(left_x, right_x + 1):
            ground_matrix[y][ix] = '~'
        y -= 1
    
    for ix in range(left_x, right_x + 1):
        ground_matrix[y][ix] = '|'
    
    # recursive drop
    if not hit_left_wall:
        drop_to_next_clay_or_water(left_x, y)
    if not hit_right_wall:
        drop_to_next_clay_or_water(right_x, y)

def print_ground():
    for y in range(1900):
        line = ""
        for x in range(220):
            line += ground_matrix[y][x]
        print(line)
    print()

drop_to_next_clay_or_water(init_x, init_y)

reachable = 0
retained = 0

# ignore "|" before first clay (hardcoded, sorry D:)
for y in range(7, 1900):
    for x in range(0, 220):
        if ground_matrix[y][x] == '|':
            reachable += 1
        if ground_matrix[y][x] == '~':
            reachable += 1
            retained += 1

#print_ground()
print(reachable)
print(retained)