import sys
from collections import defaultdict
from itertools import combinations

inf = sys.argv[1] if len(sys.argv) > 1 else "input"
input = open(inf).readlines()
locations = defaultdict(list)

nrows = len(input)
ncols = len(input[0]) - 1

# Represent antenna location as complex number
# Origin is the upper leftmost square, imaginary
# axis goes down, real axis to the right
for i_row, line in enumerate(input):
    line = line.rstrip("\n")
    for i_col, c in enumerate(line):
        if c != '.':
            locations[c].append(complex(i_col, i_row))

antinode_locations_part1 = set()
antinode_locations_part2 = set()

for antenna, locs in locations.items():
    for l1, l2 in combinations(locs, 2):
        diff = l1 - l2
        mul = 0
        while True:
            antinode = l2 - mul * diff
            if not (0 <= antinode.imag < nrows and 0 <= antinode.real < ncols):
                break
            if mul == 1:
                antinode_locations_part1.add(antinode)
            antinode_locations_part2.add(antinode)
            mul += 1

        mul = 0
        while True:
            antinode = l1 + mul * diff
            if not (0 <= antinode.imag < nrows and 0 <= antinode.real < ncols):
                break
            if mul == 1:
                antinode_locations_part1.add(antinode)
            antinode_locations_part2.add(antinode)
            mul += 1
        

print(len(antinode_locations_part1))
print(len(antinode_locations_part2))

