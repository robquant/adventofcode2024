import re
from collections import Counter

numbers = [map(int, re.findall(r'\d+', line)) for line in open("input")]
col1, col2 = zip(*numbers)

# Part 1
s = 0
for n1, n2 in zip(sorted(col1), sorted(col2)):
    s += abs(n1 - n2)

print(s)

# Part 2
similarity = 0
counts = Counter(col2)
for n in col1:
    similarity += n * counts[n]

print(similarity)
