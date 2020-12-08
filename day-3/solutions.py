import numpy as np

# PART 1

geo = np.genfromtxt("input.txt",dtype=str,comments=None)

h_position = 0
m = len(geo[0])
trees = 0
for i in geo:
    if i[h_position] == "#":
        trees+=1
    h_position = (h_position + 3) % m

print(f"Part 1: Number of trees {trees}")

# PART 2

slopes = np.array([[1,1],[3,1],[5,1],[7,1],[1,2]])
trees = np.zeros(slopes.shape[0],dtype=int)
for i1,i2 in enumerate(slopes):
    h_position = 0
    t_trees = 0
    for v,u in enumerate(geo):
        if v % i2[1] == 0:
            if u[h_position] == "#":
                t_trees+=1
            h_position = (h_position + i2[0]) % m
    trees[i1] = t_trees

print(f"Part 2: Product of trees encountered {trees.prod()}")

