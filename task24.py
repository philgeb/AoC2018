import re
import copy

class Group:
    def __init__(self, units, hp, dmg, ini, weaks, imms, dmg_type, is_immune_sys_group):
        self.units = units
        self.hp = hp
        self.dmg = dmg
        self.ini = ini
        self.weaks = weaks
        self.imms = imms
        self.dmg_type = dmg_type
        self.is_immune_sys_group = is_immune_sys_group
        self.has_units = True

def parse(init_groups):
    f = open("input24.txt", "r")

    is_immune_sys_group = True

    for l in f.read().splitlines():
        if l == '' or l[0] == 'I':
            if "Infection" in l:
                is_immune_sys_group = False
            continue

        units, hp, dmg, ini = map(int, re.findall(r'\d+', l))
        weak_match = re.search(r'weak to ([a-z, ]*)', l)
        weaknesses = []
        if weak_match:
            weaknesses = weak_match.group(1).split(", ")
        
        immune_match = re.search(r'immune to ([a-z, ]*)', l)
        immunities = []
        if immune_match:
            immunities = immune_match.group(1).split(", ")

        dmg_type_match = re.search(r'([a-z]*) damage', l)
        dmg_type = dmg_type_match.group(1)

        init_groups.append(Group(units, hp, dmg, ini, weaknesses, immunities, dmg_type, is_immune_sys_group))

# return True/False if immune system resp. infections won and sum of surviving units, e.g (True, 5400), (False, 3600)
def simulate(init_groups, boost=0):
    groups = copy.deepcopy(init_groups)

    if boost > 0:
        for g in groups:
            if g.is_immune_sys_group:
                g.dmg += boost

    immune_sys = list(filter(lambda g: g.is_immune_sys_group, groups))
    infections = list(filter(lambda g: not g.is_immune_sys_group, groups))
    while immune_sys and infections:

        ### target phase

        # highest effective power groups choose first, ties are broken based on initiative
        groups.sort(key=lambda g: g.ini)
        groups.sort(key=lambda g: g.units * g.dmg)
        groups.reverse()

        already_defended_this_round = []
        attacker_to_defender = {}
        for g in groups:
            possible_targets = []
            enemies = infections if g.is_immune_sys_group else immune_sys
            for e in enemies:
                if e not in already_defended_this_round and g.dmg_type not in e.imms:
                    possible_targets.append(e)

            if not possible_targets:
                continue
            
            # tie breaking: focus on targets that take double dmg
            possible_weak_targets = list(filter(lambda t: g.dmg_type in t.weaks, possible_targets))
            if possible_weak_targets:
                possible_targets = possible_weak_targets
            
            # tie breaking: focus on targets with highest eff dmg
            highest_effective_dmg = max(t.dmg * t.units for t in possible_targets)
            possible_targets = list(filter(lambda t: t.dmg * t.units == highest_effective_dmg, possible_targets))

            # tie breaking: focus on higher initiative
            possible_targets.sort(key=lambda t: t.ini, reverse=True)

            chosen_enemy = possible_targets[0]
            already_defended_this_round.append(chosen_enemy)
            attacker_to_defender[g] = chosen_enemy

        ### attack phase

        # highest initiative attacks first
        groups.sort(key=lambda g: g.ini, reverse=True)

        attack_occured_this_round = False
        for g in groups:
            if g in attacker_to_defender and g.has_units:
                defender = attacker_to_defender[g]
                dmg = g.units * g.dmg

                if g.dmg_type in defender.weaks:
                    dmg *= 2

                killed_units = dmg // defender.hp
                defender.units -= killed_units

                if defender.units <= 0:
                    defender.has_units = False

                if killed_units > 0:
                    attack_occured_this_round = True

        # prevent 2 possible infinite loops:
        # either only groups remain that are immune to each other
        # or none of the remainig groups have enough dmg to kill at least 1 unit of there target
        if not attack_occured_this_round:
            return (None, None)

        # remove dead groups
        groups = list(filter(lambda g: g.has_units, groups))
        immune_sys = list(filter(lambda g: g.has_units, immune_sys))
        infections = list(filter(lambda g: g.has_units, infections))

    sum_surviving_units = 0
    for g in groups:
        sum_surviving_units += g.units
    
    return (immune_sys != [], sum_surviving_units)

def part1():
    init_groups = []
    parse(init_groups)
    immune_won, sum_survs = simulate(init_groups)
    print(sum_survs)

def part2():
    init_groups = []
    parse(init_groups)

    boost = 1
    while True:
        print(boost)
        immune_won, sum_survs = simulate(init_groups, boost=boost)
        if immune_won:
            print(sum_survs)
            break
        boost += 1

part2()
