import numpy as np
from functools import lru_cache 

with open("puzzle.txt") as f:
    line = np.array([int(n) for n in f.read().split()], dtype=np.int64)



@lru_cache(maxsize=None)
def blink(stone):

    textStone = str(stone)


    if stone == 0:
        return (1, None) # Left / Right

    elif (length := len((tmp := str(stone)))) % 2 == 0:
        mid = length // 2
        left = int(tmp[:mid])
        right = int(tmp[mid:])
        return (left, right)

    else:
        return (stone*2024, None)


@lru_cache(maxsize=None)
def all_blink_for_one_stone(stone, depth):
    
    left, right = blink(stone)

    if depth == 1:
        if right is None:
            return 1
        else:
            return 2

    else:

        output = all_blink_for_one_stone(left, depth-1)
        if right is not None:
            output += all_blink_for_one_stone(right, depth-1)

        return output

def start(n, allStones):
    output = 0

    for stone in allStones:
        output += all_blink_for_one_stone(stone, n)

    return output 


result1 = start(25, line)
print(f"{result1=}")
result2 = start(75, line)
print(f"{result2=}")
