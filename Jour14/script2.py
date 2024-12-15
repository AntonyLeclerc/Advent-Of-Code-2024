import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

#file = "puzzle_ex.txt"
#shape1 = (7,11)

file = "puzzle.txt"
shape2 = (103,101)
with open(file) as f:
    lines = np.array([s.split(' ') for s in f.read().splitlines()])

area = np.zeros(shape2).astype(np.int32)


loc_and_speeds = []

for p, v in lines:
    x, y = list(map(int, p[2:].split(',')))
    dx, dy = list(map(int, v[2:].split(',')))

    loc_and_speeds.append([[x, y], [dx, dy]])


for (x, y), _ in loc_and_speeds:
    area[y, x] += 1

def update(M, y, x, dy, dx):
    cols, rows = M.shape
    newY, newX = (y+dy)%cols, (x+dx)%rows
    M[y, x] -= 1
    M[newY, newX] += 1
    
    return newY, newX


print(f"{area.shape=}")
second = 1
rows, cols = area.shape
for second in range(9999):
    if second % 200 == 0:
        print(f"{second=}")
    for i in range(len(loc_and_speeds)):
        (x, y), (dx, dy) = loc_and_speeds[i]
        newY, newX = update(area, y, x, dy, dx)

        loc_and_speeds[i][0] = [newX, newY]

    tmp = np.copy(area)
    tmp = np.where(tmp == 0, 0, 255)
    cv.imwrite(f"images/{second+1}.png", tmp.astype(np.uint8))