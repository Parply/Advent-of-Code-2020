import re
from collections import defaultdict

with open("input.txt","r") as f:
    data= [i.rstrip() for i in f.read().splitlines()]


cur_floor = defaultdict(lambda: False)

for line in data:
    co = re.findall(r"e|se|sw|sw|w|nw|ne", line)
    ns = co.count("se") + co.count("sw") - co.count("ne") - co.count("nw")
    we = co.count("e") + co.count("ne") - co.count("w") - co.count("sw")

    cur_floor[((ns,we))] = not cur_floor[((ns,we))]

print(f"Part 1: { sum(list(cur_floor.values())) }")

adj_list = [(0, -1), (1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0)]

for _ in range(100):
    n_floor = defaultdict(lambda: False)

    for k,v in cur_floor.items():
        for o in adj_list:
            tile = (k[0]+o[0],k[1]+o[1])
            if tile not in n_floor:
                n_floor[tile] = cur_floor.get(tile,False)
    for k,v in n_floor.items():
        neighbors = sum([cur_floor[(k[0]+o[0],k[1]+o[1])] for o in adj_list])

        if v:
            if not neighbors or neighbors>2:
                n_floor[k]=False
        else:
            if neighbors == 2:
                n_floor[k]=True

    cur_floor=n_floor

print(f"Part 2: { sum(list(n_floor.values())) }")
