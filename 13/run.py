import sys
import re
import itertools

def parse_machine(lines):
    A = [int(x) for x in re.findall("[\+-]\d+", lines[0])]
    B = [int(x) for x in re.findall("[\+-]\d+", lines[1])]
    prize = [int(x) for x in re.findall("[\+-]?\d+", lines[2])]
    return A, B, prize

def solve(A, B, prize):
    xa, ya = A
    xb, yb = B
    X, Y = prize
    try:
        a = (X * yb - Y * xb) / (xa * yb - ya * xb)
        b = (X * ya - Y * xa) / (xb * ya - xa * yb)
    except ZeroDivisionError:
        return None
    return a, b

prize_A = 3
prize_B = 1
total_cost_part1 = 0
total_cost_part2 = 0

inf = sys.argv[1] if len(sys.argv) > 1 else "input"
with open(inf) as f:
    lines = f.readlines()
    while True:
        A, B, prize = parse_machine(lines)
        solution = solve(A, B, prize)
        if solution is not None:
            a, b = solution
            if int(a) == a and int(b) == b:
                total_cost_part1 += prize_A * int(a) + prize_B * int(b)
        prize = [prize[0] + 10000000000000, prize[1] + 10000000000000]
        solution = solve(A, B, prize)
        if solution is not None:
            a, b = solution
            if int(a) == a and int(b) == b:
                total_cost_part2 += prize_A * int(a) + prize_B * int(b)

        lines = lines[4:]
        if len(lines) < 3:
            break

print(total_cost_part1)
print(total_cost_part2)