import numpy as np

with open("puzzle.txt") as f:
    lines = np.array([list(s) for s in f.read().splitlines()]).astype(int)


a =  np.where(lines == 0)
zerosCoords = [(a[0][i], a[1][i]) for i in range(len(a[0]))]
def canClimb(M, x, y, currentHeight, already_climbed):
    rows, cols = M.shape

    cpt = 0
    if M[x, y] == 9 and (x,y):
        already_climbed.add((x,y))
        return 1

    else:
        if x > 0 and M[x-1, y] == currentHeight+1:
            cpt += canClimb(M, x-1, y, currentHeight+1, already_climbed)

        if x < rows-1 and M[x+1, y] == currentHeight+1:
            cpt += canClimb(M, x+1, y, currentHeight+1,already_climbed)

        if y > 0 and M[x, y-1] == currentHeight+1 and y > 0:
            cpt += canClimb(M, x, y-1, currentHeight+1,already_climbed)

        if y < cols-1 and M[x, y+1] == currentHeight+1:
            cpt += canClimb(M, x, y+1, currentHeight+1,already_climbed)

    return cpt

result = 0

for (x,y) in zerosCoords:
    result += canClimb(lines, x, y , 0, set())


print(f"{result=}")