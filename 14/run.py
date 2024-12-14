import sys
import statistics

def step(guards, seconds=1):
    new_guards = []
    for guard in guards:
        pos, speed = guard
        pos_x = (pos[0] + speed[0] * seconds) % size[0]
        pos_y = (pos[1] + speed[1] * seconds) % size[1]
        new_guards.append(((pos_x, pos_y), speed))
    return new_guards


inf = sys.argv[1] if len(sys.argv) > 1 else "input"
size = (11, 7) if len(sys.argv) > 1 else (101, 103)

guards = []
for line in open(inf):
    pos, speed = line.rstrip("\n").split()
    pos = [int(x) for x in pos[pos.find("=")+1:].split(",")]
    speed = [int(x) for x in speed[speed.find("=")+1:].split(",")]
    guards.append((pos, speed))


# Part 1
horizontal_center_line = size[1] // 2 
vertical_center_line = size[0] // 2

original_guards = guards[:]

guards = step(guards, seconds=100)

guards_q1 = sum(1 for p, _ in guards if p[0] < vertical_center_line and p[1] < horizontal_center_line)
guards_q2 = sum(1 for p, _ in guards if p[0] > vertical_center_line and p[1] < horizontal_center_line)
guards_q3 = sum(1 for p, _ in guards if p[0] < vertical_center_line and p[1] > horizontal_center_line)
guards_q4 = sum(1 for p, _ in guards if p[0] > vertical_center_line and p[1] > horizontal_center_line)

print(guards_q1 * guards_q2 * guards_q3 * guards_q4)

# Part 2
guards = original_guards[:]

for i in range(1, 150):
    guards = step(guards)
    var_x = statistics.variance(p[1] for p, _ in guards)
    var_y = statistics.variance(p[0] for p, _ in guards)
    if var_x < 500:
        print("X:", i)
    if var_y < 500:
        print("Y:", i)

# The code above finds repetion of the patterns in X & Y direction
# X: 2 + a * 103
# Y: 23 + b * 101

seconds = 0
for a in range(120):
    for b in range(120):
        if 2 + a * 103 == 23 + b * 101:
            seconds = 1 + a * 103

print(seconds+1)
guards = step(original_guards, seconds=seconds+1)
pos = {p for p, _ in guards}
for y in range(size[1]):
    for x in range(size[0]):
        if (x, y) in pos:
            print("*",end="")
        else:
            print(".", end="")
    print()