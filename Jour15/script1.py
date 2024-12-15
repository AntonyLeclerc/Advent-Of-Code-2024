import numpy as np

#file = "puzzle_ex.txt"
file = "puzzle.txt"

with open(file) as f:
    lines = f.read()

maze, moves = lines.split("\n\n")
maze = np.array([np.array(list(s)) for s in maze.split('\n')])

at_coords = np.where(maze == '@')
x, y = at_coords[0][0], at_coords[1][0]

print(f"{x,y=}")

def move(M, x, y, direction):
    toMove = M[x, y]
    canMove = True
    match direction:
        case '^':
            dx, dy = -1, 0
        case '<':
            dx, dy = 0, -1
        case 'v':
            dx, dy = 1, 0
        case '>':
            dx, dy = 0, 1

    if M[x+dx, y+dy] != '#': # if no wall (#) on top of current pos
        if M[x+dx, y+dy] == 'O': # move box on top
            _, _, canMove = move(M, x+dx, y+dy, direction)
        else:
            if canMove and toMove != '#':
                M[x+dx, y+dy] = toMove

    else:
        canMove = False
        


    if canMove and toMove == '@':
        M[x+dx, y+dy] = toMove
        M[x, y] = '.'
    

    
    if canMove:
        return x+dx, y+dy, canMove

    else:
        return x, y, canMove


for direction in moves:
    if direction != '\n':
        x, y, _ = move(maze, x, y, direction)

result = 0
oCoords = np.where(maze == 'O')
coords = [(oCoords[0][i], oCoords[1][i]) for i in range(len(oCoords[0]))]

for x, y in coords:
    result += 100 * x + y

print(f"{result=}")