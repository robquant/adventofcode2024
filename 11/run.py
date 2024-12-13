import sys
from collections import defaultdict

def blink_single_stone(stone):
    num_str = str(stone)
    if stone == 0:
        yield 1
    elif len(num_str) % 2 == 0:
        yield int(num_str[:len(num_str)//2])
        yield int(num_str[len(num_str)//2:])
    else:
        yield stone * 2024

def blink(stones):
    after_blink = defaultdict(int)
    for stone, count in stones.items():
        for new_stone in blink_single_stone(stone):
            after_blink[new_stone] += count
    return after_blink

numbers = [int(x) for x in open(sys.argv[1] if len(sys.argv) > 1 else "input").read().split()]

numbers = {x: 1 for x in numbers}

for i in range(75):
    numbers = blink(numbers)
    if i == 24:
        print(sum(numbers.values()))

print(sum(numbers.values()))
