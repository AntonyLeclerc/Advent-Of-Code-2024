import numpy as np

with open("puzzle.txt") as f:
    lines = [np.array(list(map(int, s.split(' ')))) for s in f.read().splitlines()]

twoOk = lambda x,y : 1 <= abs(x-y) <= 3
cpt = 0 # # of safe

for report in lines:
    for i in range(len(report)):
        tmp = report
        tmp = np.delete(tmp, i)
        decreasing = np.all([tmp[i] > tmp[i+1] for i in range(len(tmp)-1)])
        increasing = np.all([tmp[i] < tmp[i+1] for i in range(len(tmp)-1)])
        if np.all([twoOk(tmp[i], tmp[i+1]) for i in range(len(tmp)-1)]) and (decreasing or increasing):
            cpt += 1
            break
        

    
print(cpt)