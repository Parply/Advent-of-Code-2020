import numpy as np

data=[]

with open("input.txt","r") as f:
    for i in f.readlines():
        data.append(i.rstrip().split(","))

earliestTime = int(data[0][0])
buses = np.array([int(i) for i in data[1] if i!='x'])
cont =True
time = earliestTime
while cont:
    for i in buses:
        if not time % i:
            cont = False
            ans = i * (time - earliestTime)
            print(f"Part 1: {ans}")
    time +=1


mods = {bus: -i % bus for i, bus in enumerate(["x" if x=="x" else int(x) for x in data[1]]) if bus != "x"}
vals = list(reversed(sorted(mods)))
val = mods[vals[0]]
r = vals[0]

for b in vals[1:]:
    while val % b != mods[b]:
        val += r
    r *= b

print(f"Part 2: {val}")
