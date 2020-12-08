import numpy as np

# PART 1

data = np.genfromtxt("input.txt",dtype=str)
executed = np.zeros(data.shape[0],dtype=int)
i = 0 
acc = 0

while True:

    executed[i] += 1
    if any(executed==2):
        break
    i1,i2=data[i]
    if i1 == "acc":
        acc += int(i2)
        i+=1
    elif i1 == "jmp":
        i += int(i2)
    elif i1 == "nop":
        i+=1
print(f"Part 1: acc {acc}")

# PART 2

data[-1][1] = "+1"

mdata = data.copy()


candidates = executed >=1

nops = np.where((mdata[:,0] == "nop")*candidates)[0]
jmps = np.where((mdata[:,0] == "jmp")*candidates)[0]

f = True
# JMP TO NOP
    


for r in jmps:
    mdata = data.copy()
    
    mdata[r][0]="nop"

    executed = np.zeros(data.shape[0],dtype=int)
    i = 0 
    acc = 0


    while i<data.shape[0]:

        executed[i] += 1
        if any(executed==2):
            break
        i1,i2=mdata[i]
        if i1 == "acc":
            acc += int(i2)
            i+=1
        elif i1 == "jmp":
            i += int(i2)
        elif i1 == "nop":
            i+=1
    if all(executed<=1):
        failed = False
        print(f"Part 2: acc {acc}")

if failed:
    for r in nops:
        mdata = data.copy()
    
        mdata[r][0]="jmp"
        for s in range(-r,-1):
            m2data = mdata.copy()
            m2data[r][1] = str(i)
            executed = np.zeros(data.shape[0],dtype=int)
            i = 0 
            acc = 0


            while i<data.shape[0]:

                executed[i] += 1
                if any(executed==2):
                    break
                i1,i2=m2data[i]
                if i1 == "acc":
                    acc += int(i2)
                    i+=1
                elif i1 == "jmp":
                    i += int(i2)
                elif i1 == "nop":
                    i+=1
            if all(executed<=1):
                failed= False
                print(f"Part 2: acc {acc}")
            if failed == False:
                break
            
        for s in range(2,data.shape[0]-i):
            m2data = mdata.copy()
            m2data[r][1] = str(i)
            executed = np.zeros(data.shape[0],dtype=int)
            i = 0 
            acc = 0


            while i<data.shape[0]:

                executed[i] += 1
                if any(executed==2):
                    break
                i1,i2=m2data[i]
                if i1 == "acc":
                    acc += int(i2)
                    i+=1
                elif i1 == "jmp":
                    i += int(i2)
                elif i1 == "nop":
                    i+=1
            if all(executed<=1):
                failed=False
                break
                print(f"Part 2: acc {acc}")




