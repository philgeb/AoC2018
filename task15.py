from collections import deque
import copy

# sorted by reading order
def get_free_adjacents(pos_x, pos_y):
    free_adjacents = []
    for x, y in [(pos_x, pos_y - 1), (pos_x - 1, pos_y), (pos_x + 1, pos_y), (pos_x, pos_y + 1)]:
        if field[x][y] == '.':
            free_adjacents.append((x, y))
    return free_adjacents

class Unit:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type # 'E': elf, 'G': goblin
        self.hp = 200
        self.alive = True

    # if multiple adjacent enemies, result will be ordered by reading order
    def get_adjacent_enemies(self, enemies):
        adjacent_enemies = []
        enemie_type = 'G' if self.type == 'E' else 'E'
        for pos_x, pos_y in [(self.x, self.y - 1), (self.x - 1, self.y), (self.x + 1, self.y), (self.x, self.y + 1)]:
            if field[pos_x][pos_y] == enemie_type:
                adjacent_enemies.extend(filter(lambda u: u.x == pos_x and u.y == pos_y, enemies))
        return adjacent_enemies

    # BFS, returns shortest path to target
    def find_path(self, target):
        start = (self.x, self.y)
        seen = set()
        seen.add(start)
        queue = deque()
        queue.append((start, [start]))
        while (queue):
            pos, path = queue.popleft()
            if pos == target:
                return path
            for next_pos in get_free_adjacents(pos[0], pos[1]):
                if next_pos not in seen:
                    new_path = list(path)
                    new_path.append(next_pos)
                    seen.add(next_pos)
                    queue.append((next_pos, new_path))
        return [] # no path = unreachable

    def find_nearest_paths(self, enemy):
        in_range = get_free_adjacents(enemy.x, enemy.y)

        paths = []
        for pos in in_range:
            path = self.find_path(pos)
            if (len(path) > 0):
                paths.append(path)

        return paths

    def move(self, enemies):
        nearest_paths_for_each_enemy = []
        for e in enemies:
            nearest_paths_for_each_enemy.extend(self.find_nearest_paths(e))
        
        if nearest_paths_for_each_enemy == []:
            return # skip turn

        min_dist = min(len(p) for p in nearest_paths_for_each_enemy)
        nearest_paths_for_all_enemies = list(filter(lambda p: len(p) == min_dist, nearest_paths_for_each_enemy))
        
        # p[-1] is the target of each path, and [0] (resp. [1]) denotes the x resp. y coord of path node
        nearest_paths_for_all_enemies.sort(key=lambda p: p[-1][0])
        nearest_paths_for_all_enemies.sort(key=lambda p: p[-1][1])

        chosen_path = nearest_paths_for_all_enemies[0]

        # the 1st (id 0) coords of the path are the start coords, so the 2nd (id 1) are coords where we want to move
        move_x, move_y = chosen_path[1]

        # update unit coords and field
        field[self.x][self.y] = '.'
        field[move_x][move_y] = self.type
        self.x = move_x
        self.y = move_y

    def attack(self, adjacent_enemies):
        # adjacent_enemies are already in reading order, so with 2 enemies having same low hp, min will return the correct one according to reading order
        enemy_to_attack = min(adjacent_enemies, key=lambda e: e.hp)

        if self.type == 'G':
            enemy_to_attack.hp -= 3
        else:
            enemy_to_attack.hp -= elf_dmg

        if enemy_to_attack.hp <= 0:
            enemy_to_attack.alive = False
            field[enemy_to_attack.x][enemy_to_attack.y] = '.'

    def action(self):
        if not self.alive:
            return

        alive_enemies = list(filter(lambda unit: (unit.type != self.type) and unit.alive, units))
        
        # attack directly if possible, otherwise move first
        adjacent_enemies = self.get_adjacent_enemies(alive_enemies)
        if not adjacent_enemies:
            self.move(alive_enemies)
            adjacent_enemies = self.get_adjacent_enemies(alive_enemies)

        if adjacent_enemies:
            self.attack(adjacent_enemies)

def print_map():
    for x in range(field_size):
        line = ''
        for y in range(field_size):
            line += field[y][x]
        print(line)

    hps = ""
    for u in units:
        hps += u.type + ":" + str(u.hp) + " "
    print(hps + "\n")

def simulate(init_field, init_units):
    global field, units
    field = copy.deepcopy(init_field)
    units = copy.deepcopy(init_units)
    rounds = 0
    elfs_alive = True
    goblins_alive = True
    killed_elves = []
    while elfs_alive and goblins_alive:
        units.sort(key=lambda u: u.x)
        units.sort(key=lambda u: u.y)

        for u in units:
            u.action()

        # for part 1, remove this check and simulate with elf_dmg 3
        killed_elves = list(filter(lambda u: not u.alive and u.type == 'E', units))
        if (killed_elves):
            return (-1, -1)

        units = list(filter(lambda u: u.alive, units))

        elfs_alive = list(filter(lambda u: u.type == 'E', units))
        goblins_alive = list(filter(lambda u: u.type == 'G', units))

        #print_map()
        rounds += 1

    sum_hp = 0
    for u in units:
        sum_hp += u.hp

    return (rounds - 1, sum_hp)

field_size = 32
init_field = [['#' for _ in range(field_size)] for _ in range(field_size)]
init_units = []

f = open("input15.txt", "r")

y = 0
for l in f.read().splitlines():
    x = 0
    for c in l:
        if c == 'E' or c == 'G':
            init_units.append(Unit(x, y, c))
        init_field[x][y] = c
        x += 1
    y += 1

elf_dmg = 4
while True:
    rounds, sum_hp = simulate(init_field, init_units)
    if rounds != -1:
        break
    print("Failed with: " + str(elf_dmg))
    elf_dmg += 1

print(rounds)
print(sum_hp)
print(rounds * sum_hp)
