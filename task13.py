import itertools
import sys

class Cart:

    state_to_new_dir = {"^\\" : "<",
                        "^/"  : ">",
                        "^+<" : "<",
                        "^+|" : "^",
                        "^+>" : ">",
                        ">\\" : "v",
                        ">/"  : "^",
                        ">+<" : "^",
                        ">+|" : ">",
                        ">+>" : "v",
                        "v\\" : ">",
                        "v/"  : "<",
                        "v+<" : ">",
                        "v+|" : "v",
                        "v+>" : "<",
                        "<\\" : "^",
                        "</"  : "v",
                        "<+<" : "v",
                        "<+|" : "<",
                        "<+>" : "^"}

    def __init__(self, x, y, dir, occupied):
        self.x = x
        self.y = y
        self.dir = dir
        self.inter_dir = itertools.cycle(["<", "|", ">"]) # left, straight, right
        self.occupied_track = occupied

    # return collision location if collision occurs, otherwise None
    def move(self):
        if self.dir == "^":
            (new_x, new_y) = (self.x, self.y - 1)
        elif self.dir == ">":
            (new_x, new_y) = (self.x + 1, self.y)
        elif self.dir == "v":
            (new_x, new_y) = (self.x, self.y + 1)
        else: # "<"
            (new_x, new_y) = (self.x - 1, self.y)

        next_field = track_matrix[new_x][new_y]
        curr_state = self.dir + next_field
        if next_field == '+':
            curr_state += next(self.inter_dir)
        
        new_dir = self.state_to_new_dir.get(curr_state, self.dir)

        # collision check
        if next_field in ["^", ">", "v", "<"]:
            return (new_x, new_y)

        track_matrix[self.x][self.y] = self.occupied_track
        self.x = new_x
        self.y = new_y
        self.dir = new_dir
        self.occupied_track = track_matrix[new_x][new_y]
        track_matrix[new_x][new_y] = new_dir


track_size = 150

f = open("input13.txt", "r")

# for locations that contain a cart, 5 is added (e.g. 7: | and cart)
track_matrix = [[" " for _ in range(track_size)] for _ in range(track_size)]

carts = []

y = 0
for l in f.read().splitlines():
    x = 0
    for c in l:
        if c in ["<", ">"]:
            carts.append(Cart(x, y, c, "-"))
        elif c in ["^", "v"]:
            carts.append(Cart(x, y, c, "|"))
        track_matrix[x][y] = c
        x += 1
    y += 1

def print_map():
    for x in range(track_size):
        line = ''
        for y in range(track_size):
            line += track_matrix[y][x]
        print(line)

while(len(carts) > 1):
    carts.sort(key=lambda c: c.x)
    carts.sort(key=lambda c: c.y)

    i = 0
    while (i < len(carts)):
        curr = carts[i]
        collision = curr.move()

        # for part1 solution print the coordinates of the first collision
        if collision:
            # remove colliding carts instantly
            hit_cart = [c for c in carts if c.x == collision[0] and c.y == collision[1]][0]
            hit_index = carts.index(hit_cart)
            carts.remove(hit_cart) # cart getting hit
            carts.remove(curr) # cart reponsible for crash
            track_matrix[curr.x][curr.y] = curr.occupied_track
            track_matrix[hit_cart.x][hit_cart.y] = hit_cart.occupied_track
            if hit_index < i:
                i -= 1
        else:
            i += 1

# part 2 solution
print(str(carts[0].x) + "," + str(carts[0].y))