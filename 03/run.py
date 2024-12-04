import re


input = open("input").read()

all_sum = 0
controlled_sum = 0

enabled = True
for m in re.finditer("mul\((\d+),(\d+)\)|do\(\)|don't\(\)", input):
    if m.group() == "do()":
        enabled = True
    elif m.group() == "don't()":
        enabled = False
    else:
        a, b = int(m.group(1)), int(m.group(2))
        all_sum += a * b
        if enabled:
            controlled_sum += a * b

print("Part 1:", all_sum)
print("Part 2:", controlled_sum)
