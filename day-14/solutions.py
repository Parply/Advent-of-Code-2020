data =[]

with open("input.txt","r") as f:
    for i in f.readlines():
        data.append(i.rstrip().replace(" ","").split("="))

bintostr = lambda x: list(bin(x)[2:].zfill(36))

mem = {}

for i in data:
    if i[0] == "mask":
        currentmask = i[1]

    else:
        p = i[0][4:-1]

        val = bintostr(int(i[1]))
        for v,j in enumerate(currentmask):
            if j != "X":
                val[v] = j
        mem[p] = val
s=0
for i in mem.values():
    s+=int("".join(i),2)


print(f"Part 1: {s}")

mem= {}

for i in data:
    if i[0] == "mask":
        currentmask = i[1]

    else:
        p = i[0][4:-1]

        val = int(i[1])
        add = bintostr(int(p))
        for v,j in enumerate(currentmask):
            if j == "X":
                add[v] = "X"
            elif j == "1":
                add[v] = "1"

        add = "".join(add)
        nposs = add.count("X")
        flucts = []
        for j in range(2**nposs):
            flucts.append(list(bin(j)[2:].zfill(nposs)))

        for f in flucts:
            i=0
            nadd = ""
            for a in add:
                if a == "X":
                    nadd += str(f[i])
                    i+=1
                else:
                    nadd+=str(a)
            mem[int(nadd,2)] = val
s = sum(mem.values())
print(f"Part 2: {s}")
