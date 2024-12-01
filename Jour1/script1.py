import numpy as np

with open("puzzle.txt") as f:
    lines = np.array([np.array(list(map(int, s.split('   ')))) for s in f.read().splitlines()])


lines.sort(axis=0)

distances = abs(np.diff(lines))

print(f"result = {sum(distances.reshape(len(distances)))}")