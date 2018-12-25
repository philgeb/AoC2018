import re

class Point:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

def add_to_constellations(new_p):
    applicable_constellations = []
    for c in constellations:
        for p in c:
            if abs(new_p.a - p.a) + abs(new_p.b - p.b) + abs(new_p.c - p.c) + abs(new_p.d - p.d) <= 3:
                applicable_constellations.append(c)
                break
    
    if applicable_constellations:
        const_to_extend = applicable_constellations.pop(0)
        const_to_extend.append(new_p)
        if applicable_constellations:
            for ac in applicable_constellations:
                const_to_extend.extend(ac)
                constellations.remove(ac)
    else:
        # can't be added to any existing constellation, create new one
        constellations.append([new_p])

f = open("input25.txt", "r")

points = []

for l in f.read().splitlines():
    a,b,c,d = map(int, re.findall(r'-?\d+', l))
    points.append(Point(a,b,c,d))

# list of new_p lists
constellations = []

for p in points:
    add_to_constellations(p)   

print(len(constellations))
