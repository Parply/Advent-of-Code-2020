import re
import pandas as pd
import numpy as np
data = {}

with open("input.txt","r") as f:
    for i in f.readlines():
        s = i.rstrip()
        if s != "":
            if re.search(":", s):
                if re.search(":$", s):
                    last = s[:-1]
                else:
                    s = s.replace(" ", "")
                    last,s = s.split(":")
                    data[last] = s.split("or")
            else:
                if last in data:
                    data[last].append(s.split(","))
                else:
                    data[last] = [s.split(",")]
colnames = [i for i in data.keys() if i != "your ticket" and i != "nearby tickets"]
dfnames = [str(i) for i in range(len(colnames))]
df = pd.DataFrame(data["nearby tickets"],columns=dfnames).astype(int)
l = df.shape[0]

s=0
for i in dfnames:
    valid = 0
    for k in colnames:
        for j in data[k]:
            m1,m2 = j.split("-")
            valid += df[i].between(int(m1),int(m2))
    s+= df[i].loc[valid==0].sum()




print(f"Part 1: {s}")
df2 =df.copy()
for i in dfnames:
    valid=0
    for k in colnames:
        for j in data[k]:
            m1,m2 = j.split("-")
            valid += df2[i].between(int(m1),int(m2))
    df2 = df2.loc[valid!=0]

mapping = {}

for i in dfnames:
    mapping[i] = set()
    for k in colnames:
        valid = 0
        for j in data[k]:
            m1,m2 = j.split("-")
            valid += df2[i].between(int(m1),int(m2))
        if all(valid>0):
            mapping[i].add(k)
for i in sorted(mapping, key=lambda k: len(mapping[k])):
    this_field = next(iter(mapping[i]))
    for j in mapping:
        if i != j:
            mapping[j].discard(this_field)    

ans = 1

for i in mapping:
    if mapping[i].pop().startswith("departure"):
        ans *= int(data["your ticket"][0][int(i)])

print(f"Part 2: {ans}")
