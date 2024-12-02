import numpy as np

with open("puzzle.txt") as f:
    lines = [np.array(list(map(int, s.split(' ')))) for s in f.read().splitlines()]

twoOk = lambda x,y : 1 <= abs(x-y) <= 3
cpt = 0 # # of safe

for report in lines:
    if np.all([twoOk(report[i], report[i+1]) for i in range(len(report)-1)]) and (np.all([report[i] > report[i+1] for i in range(len(report)-1)]) or np.all([report[i] < report[i+1] for i in range(len(report)-1)])):
        # first check if 1 <= diff <= 3
        # then if all decreasing or all increasing
        cpt += 1
print(cpt)