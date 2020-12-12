import numpy as np

data = np.genfromtxt("input.txt",dtype=str)

v = 0
h = 0
directions = ["N","E","S","W"]
currentdir = 'E'
currentdirI = 1
for i in data:
    if i[0] == 'F':
        m = currentdir
    elif i[0] not in "RL":
        m=i[0]
    if i[0] not in "RL":
        if m == 'N':
            v += int(i[1:])


        elif m == 'S':
            v -= int(i[1:])


        elif m == 'E':
            h+= int(i[1:])


        elif m == 'W':
            h -= int(i[1:])

    elif i[0] == 'R':
        degrees = int(i[1:])/90
        currentdirI = int((currentdirI+degrees) % 4)
        currentdir = directions[currentdirI]
    elif i[0] == 'L':
        degrees = int(i[1:])/90
        currentdirI = int((currentdirI-degrees) % 4)
        currentdir = directions[currentdirI]

print(f"Part 1: {np.abs(h)+np.abs(v)}")



v = 0
h = 0
wv = 1
wh = 10

for i in data:
    if i[0] == 'F':
        s = int(i[1:])
        v += wv*s
        h += wh*s


    elif i[0] not in "RL":
        m = i[0]
        if m == 'N':
            wv += int(i[1:])
        elif m == 'S':
            wv -= int(i[1:])
        elif m == 'E':
            wh += int(i[1:])
        elif m == 'W':
            wh -= int(i[1:])

    elif i[0] == 'R':
        for i1 in range(int(i[1:])//90):
            wh,wv = wv, -wh

    elif i[0] == 'L':
        for i1 in range(int(i[1:])//90):
            wh,wv = -wv, wh

print(f"Part 2: {np.abs(h)+np.abs(v)}")
