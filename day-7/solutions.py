import numpy as np
import re 
from collections import deque
with open("input.txt","r") as f:
    data = f.read().splitlines()

bags = {}

for i in data:
    temp = re.split("bags|bag",i.replace("contain", "").replace(" ", "").replace(",","").replace(".", "") )

    temp2 = [re.sub("[0-9]","",x) for x in temp[1:-1]]


    bags[temp[0]] = set(temp2)

def walk(b,bags):
    contents = bags[b]
    if "shinygold" in contents:
        yield True
    else:
        for i in contents:
            if i != "noother":
                yield from walk(i,bags)
c=0
for i in bags.keys():
    c+= any(list(walk(i,bags)))

print(f"Part 1: Number of bags {c}")

# PART 2
bags={}
for i in data:
    temp = re.split("bags|bag",i.replace("contain", "").replace(" ", "").replace(",","").replace(".", "") )

    temp2 = temp[1:-1]
    if temp2[0] != "noother":
        bags[temp[0]] = []
        for s in temp2:
            bags[temp[0]] += [s[1:]]*int(s[0])
    else:
        bags[temp[0]] = []

def bagCount(b):
    c = len(bags[b])
    cs = []
    for k in bags[b]:
        cs.append(bagCount(k))
    return sum(cs)+c

print(f"Part 2: Number of bags {bagCount('shinygold')}")
