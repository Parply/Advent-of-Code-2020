import numpy as np

passes = np.genfromtxt("input.txt",dtype=str)
seats = np.zeros((passes.shape[0],3),dtype=int)

def helper_row(s,m1,m2):
    if s=="F":
        return m1,(m1+m2)//2
    elif s=="B":
        return (m1+m2)//2 +1, m2


def helper_column(s,m1,m2):
    if s=="L":
        return m1,(m1+m2)//2
    elif s=="R":
        return (m1+m2)//2 +1, m2

for v,i in enumerate(passes):
    m1,m2=0,127
    for s in i[:7]:
        m1,m2 = helper_row(s, m1, m2)
    if s == "F":
        seats[v,0] = m1
    elif s=="B":
        seats[v,0] = m2
    m1,m2=0,7
    for s in i[7:]:
        m1,m2 = helper_column(s, m1, m2)
    if s == "L":
        seats[v,1] = m1
    elif s == "R":
        seats[v,1] = m2
seats[:,2] = 8*seats[:,0] + seats[:,1]

print(f"Part 1: Max seat ID {seats.max()}")

# PART 2

seatids = set(seats[:,2])

for i in range(seats[:,2].min()+1,seats[:,2].max()):
    if i+1 in seatids and i-1 in seatids and i not in seatids:
        print(f"Part 2: Possible seat ID {i}")

