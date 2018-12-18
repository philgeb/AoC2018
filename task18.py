import time
import copy

area_size = 50

f = open("input18.txt", "r")

# add surrounding unusable (*) area, so corners and edges don't need special cases
area = [['*' for _ in range(area_size + 2)] for _ in range(area_size + 2)]

y = 1
for l in f.read().splitlines():
    x = 1
    for c in l:
        area[x][y] = c
        x += 1
    y += 1

def get_surrounding(x, y, char):
    res = 0
    for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if area[x + i][y + j] == char:
            res += 1
    return res

def print_area():
    for y in range(area_size + 2):
        line = ''
        for x in range(area_size + 2):
            line += area[x][y]
        print(line)

iterations = 10
for i in range(iterations):
    next_area = copy.deepcopy(area)

    for x in range (1, area_size + 1):
        for y in range(1, area_size + 1):
            if area[x][y] == '.':
                if get_surrounding(x,y,'|') >= 3:
                    next_area[x][y] = '|'
            elif area[x][y] == '|':
                if get_surrounding(x,y,'#') >= 3:
                    next_area[x][y] = '#'
            else: # lumberyard '#'
                if get_surrounding(x,y,'|') == 0 or get_surrounding(x,y,'#') == 0:
                    next_area[x][y] = '.'

    area = copy.deepcopy(next_area)

total_wood = 0
total_ly = 0
for x in range (area_size + 2):
    for y in range(area_size + 2):
        if area[x][y] == '|':
            total_wood += 1
        elif area[x][y] == '#':
            total_ly += 1

#print_area()

# part 1
print("After 10: " + str(total_wood * total_ly))

# part 2
# series repeats every 112 values starting at iteration 540
# so (1000000000 - 540) % 112 is the offset from index 540 that has to be looked at
print("After 10000000000: " + str(207998))