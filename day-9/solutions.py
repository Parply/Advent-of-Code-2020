import numpy as np

# PART 1

data = np.genfromtxt("input.txt",dtype=int)

def pairwiseSum(x):
    y=np.add.outer(x,x)
    np.fill_diagonal(y, 0)
    return y

bPairwiseSum = lambda x,y: np.any(x==y)

for i in range(25,data.shape[0]):
    if not bPairwiseSum(data[i],pairwiseSum(data[(i-25):i])):
        ans = data[i]
        print(f"Part 1: First number {ans}")
        break

# PART 2

test = lambda x: np.sum(x)==ans

x = data[:i]

for v in range(2,i):
    vals = np.convolve(x,np.ones(v,dtype=int),mode='valid')
    y = np.pad(vals,(v-1,0),'constant',constant_values=(np.nan))
    if bPairwiseSum(ans,y):
        ind=int(np.where(ans==y)[0])+1
        cand=x[(ind-v):ind]
        print(f"Part 2: Sum {cand.min()+cand.max()}")
        break




