import sys
import enum
import heapq
from dataclasses import dataclass, field

class Direction(enum.Enum):
    EAST = (0, 1)
    NORTH = (-1, 0)
    WEST = (0, -1)
    SOUTH = (1, 0)

    def rotate_counterclockwise(self):
        return {
            Direction.EAST: Direction.NORTH,
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST
        }[self]
    
    def rotate_clockwise(self):
        return {
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH,
            Direction.NORTH: Direction.EAST
        }[self]

@dataclass(eq=True, frozen=True)
class Node:
    pos: tuple[int, int]
    direction: Direction
    prev: "Node" = field(compare=False)

def read_maze(inf):
    maze = []
    for line in open(inf):
        maze.append(list(line.rstrip("\n")))
    return maze

inf = sys.argv[1] if len(sys.argv) > 1 else "input"
maze = read_maze(inf)
start, end = None, None
for irow, line in enumerate(maze):
    for icol, c in enumerate(line):
        if c == "E":
            end = (irow, icol)
        elif c == "S":
            start = (irow, icol)

count = 0
start = Node(start, Direction.EAST, prev=None)
candidates = [(0, count, start)]
count += 1
visited = set()
tiles_on_best_paths = set()
min_cost = None

while True:
    if len(candidates) == 0:
        break
    cost, _, node = heapq.heappop(candidates)
    visited.add(node)
    if node.pos == end:
        print(f"Found with cost {cost}")
        if min_cost is None:
            min_cost = cost
        if cost == min_cost:
            # Visit all nodes on the best paths
            while True:
                if node is None:
                    break
                tiles_on_best_paths.add(node.pos)
                node = node.prev 
        continue
    dy, dx = node.direction.value
    pos = node.pos
    new_pos = (pos[0] + dy, pos[1] + dx)
    if maze[new_pos[0]][new_pos[1]] != "#":
        new_node = Node(new_pos, node.direction, prev=node)
        if new_node not in visited:
            heapq.heappush(candidates, (cost + 1, count, new_node))
            count += 1
    rotated = [Node(pos, node.direction.rotate_clockwise(), prev=node), Node(pos, node.direction.rotate_counterclockwise(), prev=node)]
    for new_node in rotated:
        if new_node not in visited:
                heapq.heappush(candidates, (cost + 1000, count, new_node))
                count += 1

print(f"Found {len(tiles_on_best_paths)} tiles on the best paths")