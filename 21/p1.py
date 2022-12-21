import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile
import numpy as np
import math
import operator

cin = IStream("in")
lines = cin.all_lines()

pattern_num = compile("{}: {}")
pattern_expr = compile("{}: {} {} {}")
monkeys = dict()

def calc(monkey):
    if type(monkeys[monkey]) == int:
        return monkeys[monkey]
    op, m1, m2 = monkeys[monkey]
    return op(calc(m1), calc(m2))

ops = {
    "+": operator.add,
    "*": operator.mul,
    "-": operator.sub,
    "/": operator.floordiv
}
for line in lines:
    res = pattern_expr.parse(line)
    if res is None:
        res = pattern_num.parse(line)
        monkeys[res[0]] = int(res[1])
    else:
        monkeys[res[0]] = (ops[res[2]], res[1], res[3])

print(calc("root"))

