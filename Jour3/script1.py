import re

with open("puzzle1.txt") as f:
    line = f.read()

x = re.findall(r'mul\(\d+,\d+\)', line)
r = 0

for c in x:
    n1, n2 = map(int, re.findall(r'\d+,\d+', c)[0].split(','))
    r += n1 * n2

print(f"{r=}")