import sys
from collections import deque

inf = sys.argv[1] if len(sys.argv) > 1 else "input"

field = {}
for row, line in enumerate(open(inf)):
    for col, lot in enumerate(line.rstrip("\n")):
        field[(row, col)] = lot

def find_all_single_lots(field, start):
    visited = {}
    this_lot = set()
    queue = deque()
    queue.append(start)
    while queue:
        row, col = queue.popleft()
        if (row, col) in visited:
            continue
        visited[(row, col)] = True
        this_lot.add((row, col))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = row + dx, col + dy
            if (nx, ny) in field and field[(nx, ny)] == field[(row, col)]:
                queue.append((nx, ny))
    return this_lot, visited

def circumference(lot):
    circ = 0
    for row, col in lot:
        circ += 4
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = row + dx, col + dy
            if (nx, ny) in lot:
                circ -= 1
    return circ

def count_sides(lot):
    rows = set(row for row, _ in lot)
    cols = set(col for _, col in lot)
    sides = 0
    for row in sorted(rows):
        in_this_row = [p for p in lot if p[0] == row]
        if any((r - 1, c) not in lot for r, c in in_this_row):
            sides += 1
        if any((r + 1, c) not in lot for r, c in in_this_row):
            sides += 1
    for col in sorted(cols):
        in_this_col = [p for p in lot if p[1] == col]
        if any((r, c - 1) not in lot for r, c in in_this_col):
            sides += 1
        if any((r, c + 1) not in lot for r, c in in_this_col):
            sides += 1
    r, c = lot.pop()
    print(field[(r, c)], sides)
    return sides

def find_lots(field):
    visited = {}
    for row, col in field:
        if (row, col) in visited:
            continue
        this_lot, visited_this_lot = find_all_single_lots(field, (row, col))
        visited.update(visited_this_lot)
        yield len(this_lot), circumference(this_lot), count_sides(this_lot)

lots = list(find_lots(field))
price_part1 = sum(area * circumference for area, circumference, _ in lots)
price_part2 = sum(area * sides for area, _, sides in lots)

print(price_part1)
print(price_part2)