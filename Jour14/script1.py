import numpy as np


#file = "puzzle_ex.txt"
file = "puzzle.txt"

with open(file) as f:
    lines = np.array([s.split(' ') for s in f.read().splitlines()])

area = np.zeros((103,101)).astype(np.int32)


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


stop = False
# for each robot
for (x, y), (dx, dy) in loc_and_speeds:
    # 100 seconds
    for i in range(100):
        y, x = update(area, y, x, dy, dx)

        

print(f"Area at the end of 100 seconds : \n{area}")

rows, cols = area.shape

midRows, midCols = rows//2, cols//2

up_left = area[0:midRows, 0:midCols]
up_right = area[0: midRows, midCols+1:cols]
bottom_left = area[midRows+1: rows, 0: midCols]
bottom_right = area[midRows+1: rows, midCols+1: cols]

result = np.sum(up_left) * np.sum(up_right) * np.sum(bottom_left) * np.sum(bottom_right)

print(f"{result=}")