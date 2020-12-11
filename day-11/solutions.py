lines = []

with open("input.txt","r") as f:
    for i in f.readlines():
        lines.append(list(i.rstrip()))

rows, cols = len(lines), len(lines[0])
deltas = [(-1,-1),
        (-1,0),
        (-1,1),
        (0,-1),
        (0,1),
        (1,-1),
        (1,0),
        (1,1)]

def count(r, c, grid):
    count=0
    for i,j in deltas:
        xi,xj=r+i,c+j
        if 0<=xi<rows and 0<=xj<cols and grid[xi][xj]=='#':
            count+=1
    return count

def part1(lines,thr=4):
    while True:
        valid = True
        tgrid = [r.copy() for r in lines]
        for i,r in enumerate(tgrid):
            for j,c in enumerate(r):
                co = count(i, j, tgrid)
                if c == 'L' and co==0:
                    lines[i][j]='#'
                elif c=='#' and co>=thr:
                    lines[i][j]='L'
                valid &= (c==lines[i][j])
        if valid:
            break
    ans=0
    for i in range(rows):
        for j in range(cols):
            if lines[i][j]=='#':
                ans+=1


    print(f"Part 1: Occupied seats {ans}")
part1(lines)
lines = []

with open("input.txt","r") as f:
    for i in f.readlines():
        lines.append(list(i.rstrip()))


def count2(r, c, grid):
    count=0
    for i,j in deltas:
        xi,xj=r+i,c+j
        while 0<=xi<rows and 0<=xj<cols:
            if grid[xi][xj]=='#':
                count+=1
                break
            elif grid[xi][xj] == 'L':
                break
            xi+=i
            xj+=j
    return count

def part2(lines, thr = 5):
    while True:
        valid = True
        tgrid=[r.copy() for r in lines]
        for i, r in enumerate(tgrid):
            for j, c in enumerate(r):
                co = count2(i, j, tgrid)
                if c=='L' and co==0:
                    lines[i][j]='#'
                elif c=='#' and co>=thr:
                    lines[i][j]='L'
                valid &= (c==lines[i][j])
        if valid:
            break
    ans=0
    for i in range(rows):
        for j in range(cols):
            if lines[i][j]=='#':
                ans+=1
    print(f"Part 2: {ans}")
part2(lines)

