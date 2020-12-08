import numpy as np

# PART 1
data = [[]]
i=0
with open("input.txt","r") as f:
    for line in f:
        if line=="\n":
            data.append([])
            i+=1
        else:
            data[i].append(line.strip().replace(" ",""))
c=-1
for i in data:
    c+= np.unique(list("".join(i))).shape[0]
print(f"Part 1: Sum {c}")

# PART 2
c=1
for i in data:
    l = len(i)
    if l == 1:
        c += len(i[0])
    else:
        temp = set(i[0])
        for v in range(1,l):
            temp = temp.intersection(i[v])
        c+= len(temp)
        
print(f"Part 2: Sum {c}")

