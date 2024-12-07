import itertools
from collections import deque


def find_calibration_equations(target, numbers_, operations):
    for ops in itertools.product(operations, repeat=len(numbers_) - 1):
        numbers = deque(numbers_)

        for op in ops:
            left = numbers.popleft()
            right = numbers.popleft()
            match op:
                case '+':
                    numbers.appendleft(left + right)
                case '*':
                    numbers.appendleft(left * right)
                case '||':
                    numbers.appendleft(int(str(left) + str(right)))
                case _:
                    raise ValueError(f"Unknown operation: {op}")
            if numbers[0] > target:
                break
        if numbers[0] == target:
            return True
    return False

fullfilled_part1 = 0
fullfilled_part2 = 0
for line in open("input").readlines():
    # 10282: 9 3 7 35 587
    target, numbers = line.split(":")
    target = int(target)
    numbers = list(map(int, numbers.strip().split()))
    if find_calibration_equations(target, numbers, operations=['+', '*']):
        fullfilled_part1 += target
    if find_calibration_equations(target, numbers, operations=['+', '*', '||']):
        fullfilled_part2 += target

print(fullfilled_part1)
print(fullfilled_part2)
