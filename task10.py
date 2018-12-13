import re

class Star:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

stars = []

f = open("input10.txt", "r")
for l in f.read().splitlines():
    vals = re.findall(r'-?\d+', l)
    stars.append(Star(int(vals[0]), int(vals[1]), int(vals[2]), int(vals[3])))

def exists_at_coord(x, y):
    for s in stars:
        if s.x == x and s.y == y:
            return True
    return False

def print_stars():
    curr_leftmost = min(stars, key=lambda s: s.x)
    curr_rightmost = max(stars, key=lambda s: s.x)
    curr_bottom = min(stars, key=lambda s: s.y)
    curr_top = max(stars, key=lambda s: s.y)

    for y in range(curr_bottom.y, curr_top.y + 1):
        for x in range(curr_leftmost.x, curr_rightmost.x + 1):
            if exists_at_coord(x,y):
                print('#', end='')
            else:
                print(' ', end='')
        print("\n")

def part1():
    init_leftmost = min(stars, key=lambda s: s.x)
    init_rightmost = max(stars, key=lambda s: s.x)

    i = 0
    while (True):
        for s in stars:
            s.x += s.vx
            s.y += s.vy

        # approximation, output needs to be checked manually
        if abs(init_leftmost.x - init_rightmost.x) < 100:
            print_stars()
            print(i)
        i += 1

def part2():
    print(0)

part1()
