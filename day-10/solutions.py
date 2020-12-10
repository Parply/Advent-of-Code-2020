import numpy as np

data = np.genfromtxt("input.txt",dtype=int)
sdata = data.copy()
sdata.sort()

diffs = sdata[1:] - sdata[:-1]
d1 = np.count_nonzero(diffs==1)+1
d3 = np.count_nonzero(diffs==3)+1

print(f"Part 1: Prod {d1*d3}")
sol = {0:1}
for i in sdata:
    sol[i] = 0
    if i-1 in sol:
        sol[i] += sol[i-1]
    if i - 2 in sol:
        sol[i]+=sol[i-2]
    if i - 3 in sol:
        sol[i]+=sol[i-3]    

print(f"Part 2: {sol[sdata[-1]]}")
