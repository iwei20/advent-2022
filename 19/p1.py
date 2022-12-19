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

cin = IStream("in")
lines = cin.all_lines()

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

    search = set()
    # minute, bots: ore, clay, obsidian, geode, count: ''''
    search.add((0, 1, 0, 0, 0, 0, 0, 0, 0))
    while search:
        minute, ore_bot, clay_bot, obsidian_bot, geode_bot, ore, clay, obsidian, geode = search.pop()
        if geode + geode_bot * (24 - minute) > maximum:
            maximum = geode + geode_bot * (24 - minute)
            max_state = (minute, ore_bot, clay_bot, obsidian_bot, geode_bot, ore, clay, obsidian, geode)

        minutes_to_next_ore = math.ceil((ore_cost - ore) / ore_bot) + 1
        minutes_to_next_ore = max(minutes_to_next_ore, 1)
        if minute + minutes_to_next_ore <= 24:
            search.add((
                minute + minutes_to_next_ore, 
                ore_bot + 1, 
                clay_bot, 
                obsidian_bot, 
                geode_bot,
                ore + ore_bot * minutes_to_next_ore - ore_cost,
                clay + clay_bot * minutes_to_next_ore,
                obsidian + obsidian_bot * minutes_to_next_ore,
                geode + geode_bot * minutes_to_next_ore
            ))

        minutes_to_next_clay = math.ceil((clay_cost - ore) / ore_bot) + 1
        minutes_to_next_clay = max(minutes_to_next_clay, 1)
        if minute + minutes_to_next_clay <= 24:
            search.add((
                minute + minutes_to_next_clay, 
                ore_bot, 
                clay_bot + 1, 
                obsidian_bot, 
                geode_bot,
                ore + ore_bot * minutes_to_next_clay - clay_cost,
                clay + clay_bot * minutes_to_next_clay,
                obsidian + obsidian_bot * minutes_to_next_clay,
                geode + geode_bot * minutes_to_next_clay
            ))

        if clay_bot >= 1:
            minutes_to_next_obsidian = max(math.ceil((obsidian_cost[0] - ore) / ore_bot), math.ceil((obsidian_cost[1] - clay) / clay_bot)) + 1
            minutes_to_next_obsidian = max(minutes_to_next_obsidian, 1)
            if minute + minutes_to_next_obsidian <= 24:
                search.add((
                    minute + minutes_to_next_obsidian, 
                    ore_bot, 
                    clay_bot, 
                    obsidian_bot + 1, 
                    geode_bot,
                    ore + ore_bot * minutes_to_next_obsidian - obsidian_cost[0],
                    clay + clay_bot * minutes_to_next_obsidian - obsidian_cost[1],
                    obsidian + obsidian_bot * minutes_to_next_obsidian,
                    geode + geode_bot * minutes_to_next_obsidian
                ))

        if obsidian_bot >= 1:
            minutes_to_next_geode = max(math.ceil((geode_cost[0] - ore) / ore_bot), math.ceil((geode_cost[1] - obsidian) / obsidian_bot)) + 1
            minutes_to_next_geode = max(minutes_to_next_geode, 1)
            if minute + minutes_to_next_geode <= 24:
                search.add((
                    minute + minutes_to_next_geode, 
                    ore_bot, 
                    clay_bot, 
                    obsidian_bot, 
                    geode_bot + 1,
                    ore + ore_bot * minutes_to_next_geode - geode_cost[0],
                    clay + clay_bot * minutes_to_next_geode,
                    obsidian + obsidian_bot * minutes_to_next_geode - geode_cost[1],
                    geode + geode_bot * minutes_to_next_geode
                ))
    print(bp, "done")
    return maximum * bp

with Pool() as pool:
    qual_sum = sum(pool.imap(calculate, lines))
    print(qual_sum)
