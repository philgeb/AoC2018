import itertools
import difflib

f = open("input2.txt", "r")

def part1():
    two_letters = 0
    three_letters = 0
    for l in f.read().splitlines():
        curr = str(l)
        two_found = False
        three_found = False
        for c in curr:
            if not two_found and curr.count(c) == 2:
                two_letters += 1
                two_found = True
            if not three_found and curr.count(c) == 3:
                three_letters += 1
                three_found = True
    print(two_letters * three_letters)

def part2():
    ids = []
    for l in f.read().splitlines():
        ids.append(str(l))
    for touple in itertools.combinations(ids, 2):
        diffs = []
        str1 = str(touple[0])
        str2 = str(touple[1])
        for i in range(len(str1)):
            if (str1[i] != str2[i]):
                diffs.append(str1[i])
        if len(diffs) == 1:
            print(str1.replace(diffs[0], ""))


part2()