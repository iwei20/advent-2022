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

# op, monkey, left/right
def find(node, p=[]):
    if node == "humn":
        return p
    if type(monkeys[node]) == int:
        return None
    op, m1, m2 = monkeys[node]

    left = find(m1, p + [(op, m1, m2, 0)])
    if left is not None:
        return left
    right = find(m2, p + [(op, m1, m2, 1)])
    return right

ops = {
    "+": operator.add,
    "*": operator.mul,
    "-": operator.sub,
    "/": operator.floordiv
}

# op, yourself -> op, order
inverses = {
    (operator.add, 0): (operator.sub, 0),
    (operator.add, 1): (operator.sub, 0),
    (operator.sub, 0): (operator.add, 0),
    (operator.sub, 1): (operator.sub, 1),
    (operator.mul, 0): (operator.floordiv, 0),
    (operator.mul, 1): (operator.floordiv, 0),
    (operator.floordiv, 0): (operator.mul, 0),
    (operator.floordiv, 1): (operator.floordiv, 1)
}

for line in lines:
    res = pattern_expr.parse(line)
    if res is None:
        res = pattern_num.parse(line)
        monkeys[res[0]] = int(res[1])
    else:
        monkeys[res[0]] = (ops[res[2]], res[1], res[3])

path = find("root")
desired = calc(path[0][2 - path[0][3]])
yourself = path[0][0]
for prev, curr in windowed(path, 2):

    yourself = curr[1 + curr[3]]
    val_other = calc(curr[2 - curr[3]])

    op, order = inverses[(curr[0], curr[3])]
    if order == 0:
        desired = op(desired, val_other)
    else:
        desired = op(val_other, desired)
print(desired)
