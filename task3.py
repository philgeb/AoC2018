import re

f = open("input3.txt", "r")
matrix = [[0 for x in range(1000)] for y in range(1000)] 

for l in f.read().splitlines():
    numbers = re.findall(r'\d+', l)
    dist_left = int(numbers[1])
    dist_top = int(numbers[2])
    w = int(numbers[3])
    h = int(numbers[4])
    for i in range(w):
        for j in range(h):
            matrix[dist_left + i][dist_top + j] += 1

def part1():
    sum_overlap = 0
    for i in range(1000):
        for j in range(1000):
            if matrix[i][j] >= 2:
                sum_overlap += 1
        
    print(sum_overlap)

def check_overlap(dl, dt, w, h):
    for i in range(w):
        for j in range(h):
            if matrix[dl + i][dt + j] != 1:
                return 0
    return 1

def part2():
    # read file again, not nice, but quick solution :/
    f.seek(0)
    for l in f.read().splitlines():
        numbers = re.findall(r'\d+', l)
        dist_left = int(numbers[1])
        dist_top = int(numbers[2])
        w = int(numbers[3])
        h = int(numbers[4])
        if check_overlap(dist_left, dist_top, w, h):
            print(int(numbers[0]))

part2()