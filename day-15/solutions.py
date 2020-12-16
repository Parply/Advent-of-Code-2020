data = [1,0,16,5,17,4]
numSpoken = {}
last = None

#data = [0,3,6]
for i in range(2020):
    if i < len(data):
        last = data[i]
        numSpoken[last] = i+1
    else:
        if last not in numSpoken:
            numSpoken[last] = i
            last = 0
        else:
            b=numSpoken[last]
            numSpoken[last] = i
            last = i-b

print(f"Part 1: {last}")

data = [1,0,16,5,17,4]
numSpoken = {}
last = None

#data = [0,3,6]
for i in range(30000000):
    if i < len(data):
        last = data[i]
        numSpoken[last] = i+1
    else:
        if last not in numSpoken:
            numSpoken[last] = i
            last = 0
        else:
            b=numSpoken[last]
            numSpoken[last] = i
            last = i-b

print(f"Part 2: {last}")

