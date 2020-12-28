from collections import deque

data = [9,2,5,1,7,6,8,3,4]
l = len(data)
cups = deque(data)
for _ in range(100):
    cur = cups[0]
    dest = cups[0]-1
    if dest < 1:
        dest=l
    cups.rotate(-1)

    c1 = cups.popleft()
    c2 = cups.popleft()
    c3 = cups.popleft()

    while dest in (c1,c2,c3):
        dest= dest-1 if dest>1 else dest + l-1

    while cups[0] != dest:
        cups.rotate(-1)
    cups.rotate(-1)

    cups.append(c1)
    cups.append(c2)
    cups.append(c3)

    while cups[0]!=cur:
        cups.rotate(-1)
    cups.rotate(-1)

while cups[0] != 1:
    cups.rotate(-1)
cups.popleft()

print(f"Part 1: { ''.join([str(i) for i in cups]) }")

class linked:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

nodes = {}

last_node = None
for i in data:
    cur = linked(i)
    nodes[i] = cur

    if last_node is not None:
        last_node.right = cur
        cur.left = last_node

    last_node = cur

for i in range(len(data)+1,1_000_001):
    cur = linked(i)
    nodes[i] = cur
    if last_node is not None:
        last_node.right=cur
        cur.left=last_node

    last_node = cur

ptr = nodes[data[0]]
last_node.right = ptr
ptr.left = last_node

ptr = nodes[data[0]]

for i in range(10_000_000):
    p_val = ptr.item

    c1 = ptr.right
    c2=c1.right
    c3=c2.right
    ptr.right =c3.right
    ptr.right.left=ptr

    d_val = p_val -1 or 1_000_000
    while d_val in (c1.item,c2.item,c3.item):
        d_val = d_val-1 or 1_000_000

    d_node = nodes[d_val]
    c3.right=d_node.right
    c3.right.left=c3
    d_node.right=c1
    c1.left=d_node

    ptr=ptr.right

while ptr.item != 1:
    ptr= ptr.right

print(f"Part 2: { ptr.right.item*ptr.right.right.item }")



