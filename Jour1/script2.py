import numpy as np

with open("puzzle.txt") as f:
    lines = np.array([np.array(list(map(int, s.split('   ')))) for s in f.read().splitlines()])


c0 = lines[:, 0]
c1 = lines[:, 1]

appearancesC1 = {i:len((np.where(c1 == i))[0]) for i in c0} # # of appearance of each digit
result = sum([c0[i] * appearancesC1[c0[i]] for i in range(0,len(c0))])

print(f"result = {result}")