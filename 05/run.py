import sys
from collections import defaultdict
from functools import cmp_to_key

def parse_rule(line):
    rule = [int(item) for item in line.split("|")]
    return rule

def parse_update(line):
    pages = [int(item) for item in line.split(",")]
    return pages

def is_valid_order(update, rules) -> bool:
    order = {page:index for index, page in enumerate(update)}
    result = True
    for rule in rules:
        if not rule[0] in order or not rule[1] in order:
            continue
        if order[rule[0]] > order[rule[1]]:
            #if result:
            #    print("Order: ", update)
            #print("Violated: ", rule)
            result = False
    return result

class Comparer:

    def __init__(self, rules):
        self.rules = defaultdict(set)
        for a, b in rules:
            self.rules[a].add(b)

    def cmp(self, x, y):
        if x in self.rules:
            if y in self.rules[x]:
                return -1
        if y in self.rules:
            if x in self.rules[y]:
                return 1
        raise ValueError(f"{x} ? {y}")
        

rules = []
updates = []

inf = sys.argv[1] if len(sys.argv) > 1 else "input"

for line in open(inf):
    line = line.rstrip("\n")
    if "|" in line:
        rules.append(parse_rule(line))
    elif "," in line:
        updates.append(parse_update(line))
    else:
        pass

middle_page_sum_part1 = 0
middle_page_sum_part2 = 0
cmp = Comparer(rules)
for update in updates:
    if is_valid_order(update, rules):
        # Gives middle page due to 0-indexing
        middle_page_sum_part1 += update[len(update)//2]
    else:
        sorted_update = list(sorted(update, key=cmp_to_key(cmp.cmp)))
        middle_page_sum_part2 += sorted_update[len(sorted_update)//2]

print(middle_page_sum_part1)
print(middle_page_sum_part2)
