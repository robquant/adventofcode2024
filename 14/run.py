import sys

inf = sys.argv[1] if len(sys.argv) > 1 else "input"
size = (11, 7) if len(sys.argv) > 1 else (101, 103)

guards = []
for line in open(inf):
    pos, speed = line.rstrip("\n").split()
    pos = [int(x) for x in pos[pos.find("=")+1:].split(",")]
    speed = [int(x) for x in speed[speed.find("=")+1:].split(",")]
    guards.append((pos, speed))

positions = []
steps = 100
for guard in guards:
    pos, speed = guard
    pos_x = (pos[0] + speed[0] * steps) % size[0]
    pos_y = (pos[1] + speed[1] * steps) % size[1]
    positions.append((pos_x, pos_y))

# Count guards in each quadrant
quadrant_height = size[1] // 2
quadrant_width = size[0] // 2
