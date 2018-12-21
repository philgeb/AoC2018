# toggle for part1/part2 solution
part1 = True

# ELF code rewritten in python with appropriate control flow
r5 = 0
last = -1
seen = set()
while True:
    r3 = r5 | 65536
    r5 = 10828530
    while True:
        #r5 += r3 & 255
        #r5 &= 16777215
        #r5 *= 65899
        #r5 &= 16777215
        r5 = (((r5 + (r3 & 255)) & 16777215) * 65899) & 16777215

        if (r3 < 256):
            break
        
        # the following can be optimized
        #r2 = 0
        #while True:
        #    r1 = (r2 + 1) * 256
        #    if (r1 > r3)
        #        break
        #    r2++
        #r3 = r2
        # ... to this
        r3 = r3 // 256

    if part1:
        print(r5)
        break

    if (r5 in seen):
        print(last)
        break
    else:
        last = r5
        seen.add(r5)
