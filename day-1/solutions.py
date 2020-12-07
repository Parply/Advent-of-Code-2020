import numpy as np

# PART 1

numbers = np.genfromtxt("input.txt",dtype=int)
pairwiseSums = np.add.outer(numbers,numbers)
ind = np.where(pairwiseSums==2020)
l = ind[0].shape[0]//2
res = numbers[ind[0][:l]]*numbers[ind[1][:l]]
print(f"Part 1: Product(s) are {res}")
print(f"Part 1: Answer is {res.max()}")

pairwiseSums = np.add.outer(pairwiseSums,numbers)
ind = np.where(pairwiseSums==2020)
l = ind[0].shape[0]//3
res = numbers[ind[0][:l]]*numbers[ind[1][:l]] * numbers[ind[2][:l]]
print(f"Part 2: Product(s) are {res}")
print(f"Part 2: Answer is {res.max()}")
