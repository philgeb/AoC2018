f = open("input8.txt", "r")
values = f.read().split(' ')
it = iter(values)

class Node:
    def __init__(self):
        self.children = []
        self.metadata = []

def parse_node():
    node = Node()
    num_children = int(next(it))
    num_meta = int(next(it))
    for _ in range(num_children):
        node.children.append(parse_node())
    for _ in range(num_meta):
        node.metadata.append(int(next(it)))
    return node

def meta_sum(node):
    sum_meta = 0
    for c in node.children:
        sum_meta += meta_sum(c)
    sum_meta += sum(node.metadata)
    return sum_meta

def node_value(node):
    if len(node.children) == 0:
        return sum(node.metadata)

    value = 0
    for m in node.metadata:
        if m > 0 and m <= len(node.children):
            value += node_value(node.children[m - 1])
    return value

def part1():
    root = parse_node()
    print(meta_sum(root))

def part2():
    root = parse_node()
    print(node_value(root))

part2()