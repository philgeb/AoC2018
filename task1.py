def part1():
    freq = 0
    f = open("input1.txt", "r")
    for l in f.readlines():
        freq += int(l)
    print(freq)

def part2():
    values = []
    seen = set()
    seen.add(0)
    freq = 0
    f = open("input1.txt", "r")
    for l in f.readlines():
        values.append(int(l))
    while (1):
        for v in values:
            freq += v
            if (freq in seen):
                print(freq)
                return
            seen.add(freq)

part2()