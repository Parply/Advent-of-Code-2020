import numpy as np

# PART 1

getOcc = lambda s: s.split("-")
getLetter = lambda s: s[0]


data = np.genfromtxt("input.txt",dtype=str)

c = 0
for i in data:
    m1,m2=getOcc(i[0])
    l = getLetter(i[1])
    pas = i[2]
    temp = pas.count(l)
    if temp>=int(m1) and temp <= int(m2):
        c+=1
print(f"Part 1: Number of valid passwords {c}")

# PART 2
c = 0
for i in data:
    m1,m2=getOcc(i[0])
    l = getLetter(i[1])
    pas = i[2]
    p1 = pas[int(m1)-1] == l
    p2 = pas[int(m2)-1] == l
    if p1 is not p2:
        c+=1
print(f"Part 2: Number of valid passwords {c}")

