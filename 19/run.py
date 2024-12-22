import re

lines = [line.rstrip("\n") for line in open("input")]

towel_patterns = [p.strip(" ") for p in lines[0].split(",")]
pattern = "(" + "|".join(towel_patterns) +")+$"

print(pattern)
possible = 0
pattern = re.compile(pattern)
for design in lines[2:]:
    print("Testing",design)
    if re.match(pattern, design) is not None:
        possible += 1

print(possible)
