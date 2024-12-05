import numpy as np

with open("puzzle.txt") as f:
    lines = np.array([list(s) for  s in f.read().splitlines()])

pattern = np.array(['X','M','A','S'])

xCoords, yCoords = np.where(lines == 'X')

r = 0

rows, cols = lines.shape

def checkAllDirection(M, x, y):
    # from a X's coordinates (x,y) in M, check all direction if XMAS appears

    cpt = 0
    # number of XMAS for (x,y)

    # right
    if np.array_equal(M[x, y:y+4], pattern):
        cpt += 1

    # bottom 
    if np.array_equal(M[x:x+4, y], pattern):
        cpt += 1

    # top
    if np.array_equal(M[x-3:x+1, y][::-1], pattern):
        cpt += 1

    # left
    if np.array_equal(M[x, y-3:y+1][::-1], pattern):
        cpt += 1


    # up left diagonal
    # permits to go towards any diagonal
    diagonals = []
    if (x >= 3 and y >= 3):
        xUL, yUL = np.array([i for i in range(x-3, x+1)][::-1]), np.array([i for i in range(y-3, y+1)][::-1])
        diagonals.append(([xUL, yUL], "UL"))
    if (x <= rows - 4 and y >= 3):
        xBL, yBL = np.array([i for i in range(x, x+4)]), np.array([i for i in range(y-3, y+1)][::-1])
        diagonals.append(([xBL, yBL], "BL"))

    if (x <= rows-4 and y <= cols-4):
        xBR, yBR = np.array([i for i in range(x, x+4)]), np.array([i for i in range(y, y+4)])
        diagonals.append(([xBR, yBR], "BR"))

    if (x >= 3 and y <= cols - 4):
        xUR, yUR = np.array([i for i in range(x-3, x+1)][::-1]), np.array([i for i in range(y, y+4)])
        diagonals.append(([xUR, yUR], "UR"))

    for d, letters in diagonals:
        if np.array_equal(M[d[0], d[1]], pattern):
            cpt += 1

    return cpt
    



for i in range(len(xCoords)):
    xc, yc = xCoords[i], yCoords[i]

    r += checkAllDirection(lines, xc, yc)

print(f"{r=}")