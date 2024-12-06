import sys

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
            if result:
                print("Order: ", update)
            print("Violated: ", rule)
            result = False
    return result

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

middle_page_sum = 0
for update in updates:
    if is_valid_order(update, rules):
        # Gives middle page due to 0-indexing
        middle_page_sum += update[len(update)//2]

print(middle_page_sum)
