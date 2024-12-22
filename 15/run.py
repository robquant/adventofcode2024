import sys
from enum import Enum

DIRECTION = {
    "^" : (-1, 0),
    ">" : (0, 1),
    "v" : (1, 0),
    "<" : (0, -1)
}

def move_robot(warehouse, robot, direction):
    step = DIRECTION[direction]
    new_robot = [robot[0] + step[0], robot[1] + step[1]]
    # No need to check if we move out of bounds as the warehouse is surrounded by walls
    if warehouse[new_robot[0]][new_robot[1]] == "#":
        return robot
    if warehouse[new_robot[0]][new_robot[1]] == ".":
        return new_robot

    # Check if we can push a box
    nboxes = 1
    while warehouse[robot[0] + nboxes * step[0]][robot[1] + nboxes * step[1]] == "O":
        nboxes += 1
    nboxes -= 1
    # Check if there is a wall behind the box
    if warehouse[robot[0] + (nboxes + 1) * step[0]][robot[1] + (nboxes + 1) * step[1]] == "#":
        return robot
    assert warehouse[robot[0] + (nboxes + 1) * step[0]][robot[1] + (nboxes + 1) * step[1]] == "."
    warehouse[robot[0] + (nboxes + 1) * step[0]][robot[1] + (nboxes + 1) * step[1]] = "O"
    warehouse[robot[0] + step[0]][robot[1] + step[1]] = "."
    return new_robot

def print_warehouse(warehouse, robot):
    for i, row in enumerate(warehouse):
        for j, cell in enumerate(row):
            if i == robot[0] and j == robot[1]:
                print("@", end="")
            else:
                print(cell, end="")
        print()

def sum_coordinates(warehouse):
    return sum(100 * i + j for i, row in enumerate(warehouse) for j, cell in enumerate(row) if cell == "O")

inf = sys.argv[1] if len(sys.argv) > 1 else 'input'
lines = open(inf).readlines()

warehouse = []
robot = [0,0]
for i_line, line in enumerate(lines):
    if len(line.rstrip('\n')) == 0:
        break
    if "@" in line:
        robot = [i_line, line.index("@")]
        line = line.replace("@", ".")
    warehouse.append(list(line.strip('\n')))

moves = ''.join(line.rstrip('\n') for line in lines[i_line + 1:])

for move in moves:
    robot = move_robot(warehouse, robot, move)
print(sum_coordinates(warehouse))