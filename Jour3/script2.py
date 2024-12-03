import re

with open("puzzle2.txt") as f:
    line = f.read()


pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'
matches = re.findall(pattern, line)

r = 0
flag = True

for match in matches:
    if match == "don't()":
        flag = False
    elif match == 'do()':
        flag = True
    else:
        if flag:
            n1, n2 = map(int, re.findall(r'\d+,\d+', match)[0].split(','))
            r += n1*n2

print(f"{r=}")
