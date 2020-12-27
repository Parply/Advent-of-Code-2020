with open("input.txt","r") as f:
    d=f.read().split("\n\n")
    data={}
    data[1] = [int(i.rstrip()) for i in d[0].splitlines()[1:]]
    data[2] = [int(i.rstrip()) for i in d[1].splitlines()[1:]]



while len(data[1]) != 0 and len(data[2])!=0:
    p1 = data[1][0]
    p2 = data[2][0]
    del data[1][0]
    del data[2][0]
    if p1>p2:
        data[1].append(p1)
        data[1].append(p2)
    elif p2>p1:
        data[2].append(p2)
        data[2].append(p1)

if len(data[1]) !=0:
    win = data[1]
else:
    win = data[2]

s = 0
l = len(win)
for v,i in enumerate(win):
    s += i * (l-v)

print(f"Part 1: {s}")

with open("input.txt","r") as f:
    d=f.read().split("\n\n")
    data={}
    data[1] = [int(i.rstrip()) for i in d[0].splitlines()[1:]]
    data[2] = [int(i.rstrip()) for i in d[1].splitlines()[1:]]

previous = set()
p1 = data[1]
p2 = data[2]

def recursive_card(p1, p2, visited):
    while(len(p1) > 0 and len(p2) > 0):
        if (tuple(p1), tuple(p2)) in visited:
            return 1, p1

        visited.add((tuple(p1), tuple(p2)))

        a, b = p1.pop(0), p2.pop(0)
        if len(p1) >= a and len(p2) >= b:
            winner, _ = recursive_card(p1[:a], p2[:b], set())
        else:
            winner = 1 if a > b else 0

        if winner:
            p1.extend([a, b])
        else:
            p2.extend([b, a])
    return (1, p1) if len(p1) > 0 else (0, p2)

winner,win=recursive_card(p1, p2, previous)
s = 0
l = len(win)
for v,i in enumerate(win):
    s += i * (l-v)

print(f"Part 2: {s}")



