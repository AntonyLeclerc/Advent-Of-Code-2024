import numpy as np

with open("minipuzzle.txt") as f:
    lines = np.array([list(s) for  s in f.read().splitlines()])

xCoords, yCoords = np.where(lines == 'A')

cpt = 0
rows, cols = lines.shape

pattern1 = np.array(['M','A','S'])
pattern2 = np.array(['S','A','M'])

for i in range(len(xCoords)):

    x, y = xCoords[i], yCoords[i]

    if (x > 0 and x < rows-1 and y > 0 and y < cols-1):
        diag1 = lines[[x-1,x,x+1],[y-1,y,y+1]]
        diag2 = lines[[x+1,x,x-1],[y-1,y,y+1]]
        if (np.array_equal(diag1,diag2) and (np.array_equal(diag1, pattern1) or np.array_equal(diag1, pattern2))) or (np.array_equal(diag1,diag2[::-1]) and (np.array_equal(diag1, pattern1) or np.array_equal(diag1, pattern2))):
            cpt += 1

print(f"{cpt=}")