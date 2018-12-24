import re

class NanoBot:
    def __init__(self, x, y, z, r):
        self.x = x
        self.y = y
        self.z = z
        self.r = r

f = open("input23.txt", "r")

nanobots = []

for l in f.read().splitlines():
    x, y, z, r = list(map(int, re.findall(r'-?\d+', l)))
    nanobots.append(NanoBot(x, y, z, r))

strongest = max(nanobots, key=lambda n: n.r)

in_range = 0
for n in nanobots:
    if abs(strongest.x - n.x) + abs(strongest.y - n.y) + abs(strongest.z - n.z) <= strongest.r:
        in_range += 1

print(in_range)
