import sys
import heapq
import time


def print_memory(memory):
    for row in memory:
        print(''.join(row))

inf = sys.argv[1] if len(sys.argv) > 1 else 'input'
coordinates = []
for line in open(inf):
    x, y = map(int, line.split(','))
    coordinates.append((x, y))

memory = [['.'] * 71 for _ in range(71)]
for (x, y) in coordinates[:1024]:
    memory[y][x] = '#'

# print_memory(memory)
def dijkstra(memory, start, goal):
    rows, cols = len(memory), len(memory[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pq = [(0, start)]
    distances = {start: 0}
    while pq:
        current_distance, (x, y) = heapq.heappop(pq)
        if (x, y) == goal:
            return current_distance
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and memory[ny][nx] == '.':
                distance = current_distance + 1
                if (nx, ny) not in distances or distance < distances[(nx, ny)]:
                    distances[(nx, ny)] = distance
                    heapq.heappush(pq, (distance, (nx, ny)))
    return float('inf')

start = (0, 0)
goal = (70, 70)
start_time = time.time()
shortest_path_length = dijkstra(memory, start, goal)
print(f"Shortest path length from {start} to {goal} is {shortest_path_length}")

for (x, y) in coordinates[1024:]:
    memory[y][x] = '#'
    shortest_path_length = dijkstra(memory, start, goal)
    if shortest_path_length == float('inf'):
        print(f"Coordinate {x}, {y} blocked the path")
        break