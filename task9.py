import re
import collections

f = open("input9.txt", "r")

def part1(factor100 = False):
    line = f.read()
    vals = re.findall(r'\d+', line)
    num_players = int(vals[0])
    num_marbles = int(vals[1])
    if factor100:
        num_marbles *= 100
    marble_list = collections.deque() # way for efficient here than a normal list
    marble_list.append(0)
    player_to_score_map = {}

    for p in range(num_players):
        player_to_score_map[p] = 0

    curr_m_index = 0
    for m in range(1, num_marbles + 1):

        if m % 23 == 0:
            marble_list.rotate(8)     
            score = m + marble_list.pop()
            marble_list.rotate(-2)
            curr_player = m % num_players # last player has index 0 (e.g with 4 players it goes like: 1,2,3,0,1,2,3,0,...)
            player_to_score_map[curr_player] += score
            continue

        marble_list.append(m)
        marble_list.rotate(-1)
    
    print(max(player_to_score_map.values()))

def part2():
    part1(True)

part2()