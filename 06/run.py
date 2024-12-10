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


def walk(field, start_pos):
    nrows, ncols = len(field), len(field[0])
    pos = start_pos
    direction = (-1, 0)
    visited = {(pos, direction)}

    while True:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if new_pos[0] < 0 or new_pos[0] >= nrows or new_pos[1] < 0 or new_pos[1] >= ncols:
            break
        elif field[new_pos[0]][new_pos[1]] == "#":
            direction = turn_right(direction)
        else:
            pos = new_pos
            if field[pos[0]][pos[1]] == ".":
                if (pos, direction) in visited:
                    return True, visited
                visited.add((pos, direction))

    return False, visited

input = sys.argv[1] if len(sys.argv) > 1 else "input"
field = [list(line.rstrip("\n")) for line in open(input)]
start_pos = [(i_line, line.index("^")) for i_line, line in enumerate(field) if "^" in line][0]
print(f"Start position: {start_pos}")
_, visited = walk(field, start_pos)
distinct_pos = {pos for pos, _ in visited}
print(f"Visited {len(distinct_pos)} cells")

# Part 2
loops = 0
for cell in distinct_pos - {start_pos}:
    field[cell[0]][cell[1]] = "#"
    loop, _ = walk(field, start_pos)
    if loop:
        loops += 1
        # print(cell, loop)
    field[cell[0]][cell[1]] = "."

print(f"Found {loops} loops")