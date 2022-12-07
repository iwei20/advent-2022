import sys
sys.path.append("..")
from adventio import IStream
from collections import *
from itertools import *
from more_itertools import *
from parse import compile

from functools import reduce  # forward compatibility for Python 3
import operator

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)

def setInDict(dataDict, mapList, value):
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value

cin = IStream("in")

root = defaultdict(int)

discard = cin.next_line()
line = cin.next_line()
line_split = line.split()
currloc = []
while line:
    if line_split[0] == "$":
        if line_split[1] == "cd":
            if line_split[2] == "/":
                currloc = []
            elif line_split[2] == "..":
                currloc.pop()
            else:
                currloc.append(line_split[2])
            line = cin.next_line()
            line_split = line.split()

        elif line_split[1] == "ls":
            line = cin.next_line()
            line_split = line.split()
            while line and line_split[0] != "$":

                if line_split[0] == "dir":
                    getFromDict(root, currloc)[line_split[1]] = defaultdict(int)
                else:
                    getFromDict(root, currloc)["__sum__"] += int(line_split[0])

                line = cin.next_line()
                line_split = line.split()

def dir_size(directory: defaultdict):
    return directory["__sum__"] + sum(dir_size(subdir) for item, subdir in directory.items() if item != "__sum__")

need_to_delete = dir_size(root) - 40000000
def smallest_free_dir(directory: defaultdict):
    store_size = dir_size(directory)
    if store_size < need_to_delete:
        return 1e12
    smallest_subdir_generator = list(smallest_free_dir(subdir) for item, subdir in directory.items() if item != "__sum__")
    smallest_subdir_work = 1e12 if not smallest_subdir_generator else min(smallest_subdir_generator)
    return min(store_size, smallest_subdir_work)
print(smallest_free_dir(root))