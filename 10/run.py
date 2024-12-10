from collections import Counter

def find_paths(grid):
    rows, cols = len(grid), len(grid[0])
    paths = []

    def dfs(x, y, path):
        if grid[x][y] == '9':
            paths.append(path[:])
            return
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and int(grid[nx][ny]) == int(grid[x][y]) + 1:
                path.append((nx, ny))
                dfs(nx, ny, path)
                path.pop()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '0':
                dfs(i, j, [(i, j)])

    return paths

# grid = [
#     "89010123",
#     "78121874",
#     "87430965",
#     "96549874",
#     "45678903",
#     "32019012",
#     "01329801",
#     "10456732"
# ]

grid = [line.strip("\n") for line in open("input")]

paths = find_paths(grid)
print(len({(path[0], path[-1]) for path in paths}))
print(len(paths))