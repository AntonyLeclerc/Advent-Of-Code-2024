import numpy as np
import re
import copy
import time 

with open("puzzle.txt") as f:
    doc = f.read()

sec1, sec2 = doc.split("\n\n")


a = re.findall(fr'\d+\|.*', sec1)
sec2 = [s.split(',') for s in sec2.split('\n')]

result = 0
result2 = 0

def isUpdateOk(update):

    violations = []
    isOk = True
    for x in update:
        c = copy.deepcopy(update)
        before, after = c[0:c.index(x)], c[c.index(x)+1:]


        for b in before:
            # if b is actually after x, update uncorrect
            tmp = re.findall(rf'{x}\|{b}', sec1)
            if len(tmp) > 0:
                violations.append(tmp[0])
                isOk = False
        
        for a in after:
            # if a is actually before x, update uncorrect
            tmp = re.findall(rf'{a}\|{x}', sec1)
            if len(tmp) > 0:
                isOk = False

    return isOk, violations

def fixUpdate(update, violations):
    newOrder = copy.deepcopy(update)
    for v in violations:
        left, right = v.split('|')

        iL, iR = newOrder.index(left), newOrder.index(right)

        newOrder[iL], newOrder[iR] = newOrder[iR], newOrder[iL]

    return newOrder


cpt = 0

t1 = time.process_time()
for update in sec2:
    
    isOk, violations = isUpdateOk(update)
    
    if isOk:
        result += int(update[len(update)//2])

    else:
        tmp = copy.deepcopy(update)

        while not(isOk):
            tmp = fixUpdate(tmp, violations)
            isOk, violations = isUpdateOk(tmp)

        result2 += int(tmp[len(tmp) // 2])

t2 = time.process_time()

      
print(f"{result=}")
print(f"{result2=}")      

print(f"Temps : {t2-t1}")