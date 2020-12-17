data = []

with open("input.txt","r") as f:
    for i in f.readlines():
        data.append(list(i.rstrip()))

neighbors = lambda c: [(c[0]+i, c[1]+j, c[2]+k) 
                 for i in range(-1, 2) 
                 for j in range(-1, 2) 
                 for k in range(-1, 2) 
                 if not (i == 0 and j == 0 and k == 0)]

check = lambda c,cubes: len([x for x in neighbors(c) if cubes.get(x)=="#"])

def simSlice(cubes):
    nc = {}
    for c in cubes:
        x = check(c,cubes)
        if cubes[c] == "#":
            if x == 2 or x == 3:
                nc[c] = "#"
            else:
                nc[c] = "."
            n = neighbors(c)
            for x in n:
                if x not in cubes:
                    k = check(x,cubes)
                    if k == 3:
                        nc[x] = "#"
        elif cubes[c] == ".":
            if x==3:
                nc[c] = "#"
            else:
                nc[c] = "."
    return nc

cubes = {(i, j, 0):data[i][j] 
             for i in range(len(data)) 
             for j in range(len(data[0]))}

for i in range(6):
    cubes = simSlice(cubes)

print(f"Part 1: {list(cubes.values()).count('#')}")

cubes = {(i, j, 0, 0):data[i][j] 
             for i in range(len(data)) 
             for j in range(len(data[0]))}

neighbors2 = lambda c: [(c[0]+i, c[1]+j, c[2]+k, c[3]+w) 
                 for i in range(-1, 2) 
                 for j in range(-1, 2) 
                 for k in range(-1, 2) 
                 for w in range(-1, 2)
                 if not (i == 0 and j == 0 and k == 0 and w == 0)]

check2 = lambda c,cubes: len([x for x in neighbors2(c) if cubes.get(x)=="#"])

def simSlice2(cubes):
    nc = {}
    for c in cubes:
        x = check2(c,cubes)
        if cubes[c] == "#":
            if x == 2 or x == 3:
                nc[c] = "#"
            else:
                nc[c] = "."
            n = neighbors2(c)
            for x in n:
                if x not in cubes:
                    k = check2(x,cubes)
                    if k == 3:
                        nc[x] = "#"
        elif cubes[c] == ".":
            if x==3:
                nc[c] = "#"
            else:
                nc[c] = "."
    return nc

for i in range(6):
    cubes = simSlice2(cubes)

print(f"Part 2: {list(cubes.values()).count('#')}")
