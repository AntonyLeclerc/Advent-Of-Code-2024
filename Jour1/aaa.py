from typing import Callable
from collections import Counter

def read_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        file_content = f.readlines()
    return file_content

def parse(filename: str) -> tuple[list[int], list[int]]:
    file = read_file(filename)
    first_list: list[int] = []
    second_list: list[int] = []
    for line in file:
        splat = line.split()
        first_list.append(int(splat[0]))
        second_list.append(int(splat[1]))
    return (first_list, second_list)

def first(filename: str) -> int:
    first_list, second_list = parse(filename)
    first_list.sort(); second_list.sort()
    zipped_list = zip(first_list, second_list)
    return sum([abs(curr[0] - curr[1]) for curr in zipped_list])

def second(filename: str) -> int:
    first_list, second_list = parse(filename)
    counter = Counter(second_list)
    return sum([curr * counter[curr] for curr in first_list])


green = "\033[92m"
red = "\033[91m"
cyan = "\033[96m"
clear = "\033[0m"

def test(func: Callable[[str], int], filename: str, expected: int) -> None:
    result = func(filename)
    color = green if result == expected else red
    print(f"found {color}{result}{clear} wanted {expected}")

def real(func: Callable[[str], int], filename: str) -> None:
    result = func(filename)
    print(f"found {cyan}{result}{clear}")

real(first, "puzzle.txt")
