with open("input.txt","r") as f:
    data = [int(i) for i in f.read().splitlines()]

d = 20201227

transformed = 1
i1 = 0
while transformed != data[0]:
    transformed = transformed * 7 % d
    i1 +=1




trasformed = 1
i2=0
while transformed != data[1]:
    transformed = transformed * 7 % d
    i2 +=1

encryption = 1

for _ in range(i1):
    encryption = encryption * data[1] % d

print(f"Part 1: {encryption}")
