import re
import collections

coord_to_erosion = {}

def calc_erosion(x, y):
    pos = (x,y)
    if pos in coord_to_erosion:
        return coord_to_erosion[pos]

    if x == 0 and y == 0 or x == target_x and y == target_y:
        geo_id = 0
    elif y == 0:
        geo_id = x * 16807
    elif x == 0:
        geo_id = y * 48271
    else:
        geo_id = calc_erosion(x, y - 1) * calc_erosion(x - 1, y)

    erosion = ((geo_id + depth) % 20183)
    coord_to_erosion[pos] = erosion
    return erosion

f = open("input22.txt", "r")

depth = int(re.search(r'\d+', f.readline())[0])
target_x, target_y = map(int, re.findall(r'\d+', f.readline()))

# part1
risk = 0
for x in range(target_x + 1):
    for y in range(target_y + 1):
        risk += calc_erosion(x, y) % 3
print(risk)


# part2, greedy best first search, really slow :(
# I'll at least do A* next time, promise :>
Node = collections.namedtuple('Node', ['x', 'y', 'tool'])

def compute_neighbors(node):
    temp = [(1,0), (0,1)]
    if node.x > 0:
        temp.append((-1, 0))
    if node.y > 0:
        temp.append((0, -1))
    
    neighbors = []
    for xi, yi in temp:
        # for target node we must use the torch
        if node.x + xi == target_x and node.y + yi == target_y:
            next_tool = 1
        else:
            neighbore_type = calc_erosion(node.x + xi, node.y + yi) % 3
            if node.tool != neighbore_type:
                next_tool = node.tool
            else:
                curr_type = calc_erosion(node.x, node.y) % 3
                next_tool = 3 - curr_type - neighbore_type

        neighbors.append(Node(node.x + xi, node.y + yi, next_tool))

    return neighbors

def shortest_path(tar_x, tar_y):
    start = Node(0, 0, 1)
    nodes_to_travel_time = {start : 0}
    open_nodes = [start]
    while open_nodes:
        curr = min(open_nodes, key=lambda node: nodes_to_travel_time[node])
        if curr.x == tar_x and curr.y == tar_y:
            return nodes_to_travel_time[curr]
        
        open_nodes.remove(curr)

        for n in compute_neighbors(curr):
            if n not in nodes_to_travel_time:
                open_nodes.append(n)

            alt_travel_time = 1 if n.tool == curr.tool else 8
            alt_travel_time += nodes_to_travel_time[curr]
            if n not in nodes_to_travel_time or alt_travel_time < nodes_to_travel_time[n]:
                nodes_to_travel_time[n] = alt_travel_time

print(shortest_path(target_x, target_y))
    

