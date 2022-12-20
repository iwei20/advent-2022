import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile
import numpy as np
import math
from multiprocessing import Pool
import operator

cin = IStream("in")
lines = cin.all_lines()
lines = lines[:3]

pattern = compile("Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.")
# 0 = do nothing
# 1 = ore
# 2 = clay
# 3 = obsidian
# 4 = geode

def calculate(line):
    maximum = 0
    max_state = ()
    result = pattern.parse(line)
    bp = result[0]
    ore_cost = result[1]
    clay_cost = result[2]
    obsidian_cost = (result[3], result[4])
    geode_cost = (result[5], result[6])

    search_set = set()
    dfs = deque()
    # minute, bots: ore, clay, obsidian, geode, count: ''''
    search_set.add((0, 1, 0, 0, 0, 0, 0, 0, 0))
    dfs.append((0, 1, 0, 0, 0, 0, 0, 0, 0))
    while dfs:
        minute, ore_bot, clay_bot, obsidian_bot, geode_bot, ore, clay, obsidian, geode = dfs.pop()
        if ore_bot > 6:
            continue
        if clay_bot > 12:
            continue
        
        if geode + geode_bot * (32 - minute) > maximum:
            maximum = geode + geode_bot * (32 - minute)
            max_state = (minute, ore_bot, clay_bot, obsidian_bot, geode_bot, ore, clay, obsidian, geode)
        if obsidian_bot >= 1:
            minutes_to_next_geode = max(math.ceil((geode_cost[0] - ore) / ore_bot), math.ceil((geode_cost[1] - obsidian) / obsidian_bot)) + 1
            minutes_to_next_geode = max(minutes_to_next_geode, 1)
            if minute + minutes_to_next_geode <= 32:
                next_state = (
                    minute + minutes_to_next_geode, 
                    ore_bot, 
                    clay_bot, 
                    obsidian_bot, 
                    geode_bot + 1,
                    ore + ore_bot * minutes_to_next_geode - geode_cost[0],
                    clay + clay_bot * minutes_to_next_geode,
                    obsidian + obsidian_bot * minutes_to_next_geode - geode_cost[1],
                    geode + geode_bot * minutes_to_next_geode
                )
                if next_state not in search_set:
                    search_set.add(next_state)
                    dfs.append(next_state)
                if minute > 26:
                    continue

        if 1 <= clay_bot and obsidian_bot < geode_cost[1]:
            minutes_to_next_obsidian = max(math.ceil((obsidian_cost[0] - ore) / ore_bot), math.ceil((obsidian_cost[1] - clay) / clay_bot)) + 1
            minutes_to_next_obsidian = max(minutes_to_next_obsidian, 1)
            if minute + minutes_to_next_obsidian <= 32:
                next_state = (
                    minute + minutes_to_next_obsidian, 
                    ore_bot, 
                    clay_bot, 
                    obsidian_bot + 1, 
                    geode_bot,
                    ore + ore_bot * minutes_to_next_obsidian - obsidian_cost[0],
                    clay + clay_bot * minutes_to_next_obsidian - obsidian_cost[1],
                    obsidian + obsidian_bot * minutes_to_next_obsidian,
                    geode + geode_bot * minutes_to_next_obsidian
                )
                if next_state not in search_set:
                    search_set.add(next_state)
                    dfs.append(next_state)
                if minute > 26:
                    continue
        
        if clay_bot < obsidian_cost[1]:
            minutes_to_next_clay = math.ceil((clay_cost - ore) / ore_bot) + 1
            if minutes_to_next_clay >= 1 and minute + minutes_to_next_clay <= 32:
                next_state = (
                    minute + minutes_to_next_clay, 
                    ore_bot, 
                    clay_bot + 1, 
                    obsidian_bot, 
                    geode_bot,
                    ore + ore_bot * minutes_to_next_clay - clay_cost,
                    clay + clay_bot * minutes_to_next_clay,
                    obsidian + obsidian_bot * minutes_to_next_clay,
                    geode + geode_bot * minutes_to_next_clay
                )
                if next_state not in search_set:
                    search_set.add(next_state)
                    dfs.append(next_state)
                if minute > 26:
                    continue

        if True:
            minutes_to_next_ore = math.ceil((ore_cost - ore) / ore_bot) + 1
            minutes_to_next_ore = max(minutes_to_next_ore, 1)
            if minute + minutes_to_next_ore <= 32:
                next_state = (
                    minute + minutes_to_next_ore, 
                    ore_bot + 1, 
                    clay_bot, 
                    obsidian_bot, 
                    geode_bot,
                    ore + ore_bot * minutes_to_next_ore - ore_cost,
                    clay + clay_bot * minutes_to_next_ore,
                    obsidian + obsidian_bot * minutes_to_next_ore,
                    geode + geode_bot * minutes_to_next_ore
                )
                if next_state not in search_set:
                    search_set.add(next_state)
                    dfs.append(next_state)
                if minute > 26:
                    continue

                
    print(bp, "done")
    return maximum

with Pool() as pool:
    qual_sum = list(accumulate(pool.imap(calculate, lines), operator.mul))[-1]
    print(qual_sum)

# best attempt lower bound: 8976
# highest attempt: 14490 ()