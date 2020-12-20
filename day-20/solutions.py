import re
import numpy as np
from collections import deque
data = {}

with open("input.txt","r") as f:
    for i in f.readlines():
        s=i.rstrip()
        if s != "":
            if s[0] == "T":
                num = int(s[5:-1])
                data[num] = []
            else:
                data[num].append(list(s))

for i in data:
    data[i] = np.array(data[i])

def all_rotations(x : np.array):
    res = [x.copy()]
    for i in range(1,4):
        res.append(np.rot90(x.copy(),i))
    return res

def all_(x : np.array):
    return np.array(all_rotations(x)+all_rotations(x.transpose()))

gro={i:all_(data[i]) for i in data}
n = int(np.sqrt(len(data)))
arranged = [[0] * n for _ in range(n)]
stack = deque(reversed(list((r, c) for c in range(n) for r in range(n))))


def find_arrangement():
    if not stack:
        print(f"Part 1: {arranged[0][0][0] * arranged[-1][0][0] * arranged[0][-1][0] * arranged[-1][-1][0]}")
        return True
    r,c = stack.pop()
    for tid in list(gro):
        t_group = gro[tid]
        del gro[tid]
        for tile in t_group:
            if r>0:
                if np.any(arranged[r - 1][c][1][-1] != tile[0]):
                    continue
            if c>0:
                if list(row[-1] for row in arranged[r][c - 1][1]) != list(row[0] for row in tile):
                    continue
            arranged[r][c] = (tid, tile)
            if find_arrangement():
                return True
        gro[tid] = t_group
    stack.append((r,c))

find_arrangement()

remove_border = lambda t: t[1:-1,1:-1]

board = np.vstack([np.hstack([remove_border(tile[1]) for tile in row]) for row in arranged])

seamonster= np.array([list('                  # '), list('#    ##    ##    ###'), list(' #  #  #  #  #  #   ')])
patterns = all_(seamonster)

for pattern in patterns:
    matches=0
    H,W = pattern.shape
    ind = np.where(pattern=="#")
    for dr in range(board.shape[0] - H + 1):
        for dc in range(board.shape[1] - W + 1):
            matches += np.all(board[dr+ind[0],dc+ind[1]] == '#')
    if matches:
        tot = (board=="#").sum()
        pat = (pattern=="#").sum()
        print(f"Part 2: {tot-pat * matches}")
        break


