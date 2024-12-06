import sys

def print_field(field):
    for line in field:
        print("".join(line))

def turn_right(direction):
    match direction:
        case (0, 1): return (1, 0)
        case (1, 0): return (0, -1)
        case (0, -1): return (-1, 0)
        case (-1, 0): return (0, 1)

input = sys.argv[1] if len(sys.argv) > 1 else "input"
field = [list(line.rstrip("\n")) for line in open(input)]
nrows, ncols = len(field), len(field[0])
pos = [(i_line, line.index("^")) for i_line, line in enumerate(field) if "^" in line][0]
print(f"Start position: {pos}")
direction = (-1, 0)
visited = 1

while True:
    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
    if new_pos[0] < 0 or new_pos[0] >= nrows or new_pos[1] < 0 or new_pos[1] >= ncols:
        break
    elif field[new_pos[0]][new_pos[1]] == "#":
        direction = turn_right(direction)
    else:
        pos = new_pos
        if field[pos[0]][pos[1]] == ".":
            visited += 1
        field[pos[0]][pos[1]] = "X"
        # print_field(field)
        # print()

print(visited)