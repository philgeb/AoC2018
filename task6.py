import re

f = open("input6.txt", "r")

coords = list()
for l in f.read().splitlines():
    vals = re.findall(r'\d+', l)
    coords.append((int(vals[0]), int(vals[1])))

min_x = min(c[0] for c in coords)
min_y = min(c[1] for c in coords)
max_x = max(c[0] for c in coords)
max_y = max(c[1] for c in coords)

def part1():
    coords_to_covered = {}

    for c in coords:
        coords_to_covered[c] = 0

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            closest_dist = 10000 # initial overapprox.
            for c in coords:
                dist = abs(c[0] - x) + abs(c[1] - y)
                if dist == closest_dist:
                    two_closest = True
                elif dist < closest_dist:
                    closest_dist = dist
                    closest_coord = c
                    two_closest = False
            if not two_closest and coords_to_covered[closest_coord] != -1:
                if x == min_x or x == max_x or y == min_y or y == max_y:
                    coords_to_covered[closest_coord] = -1 # coords whose space touches border are infinite -> ignore
                else:
                    coords_to_covered[closest_coord] += 1

    print(max(coords_to_covered.values()))

def part2():
    region_size = 0

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            total_dist = 0
            for c in coords:
                total_dist += abs(c[0] - x) + abs(c[1] - y)
            if (total_dist < 10000):
                region_size += 1
    print(region_size)

part2()
