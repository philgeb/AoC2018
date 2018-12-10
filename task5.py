import string

f = open("input5.txt", "r")

input = str(f.read())

def reduce_poly(poly):
    i = 0
    while poly[i+1] != '\n':
        if poly[i] == poly[i+1].swapcase():
            poly = poly[:i] + poly[(i+2):]
            i -= 1
        else:
            i += 1
    return len(poly) - 1 # -1 for newline

def part1():
    print(reduce_poly(input))

def part2():
    min_len = 10000 # should pos inf, but good enough initial here
    for c in string.ascii_lowercase:
        temp = input.replace(c, '').replace(c.swapcase(), '')
        curr_len = reduce_poly(temp)
        min_len = min(min_len, curr_len)
    
    print(min_len)

part2()
        