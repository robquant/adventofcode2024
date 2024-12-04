
def find(input, row, col, d, target):
    if target == "":
        return True
    if row < 0 or row >= len(input) or col < 0 or col >= len(input[0]):
        return False
    if input[row][col] != target[0]:
        return False
    return find(input, row + d[0], col + d[1], d, target[1:])

input = [line.rstrip("\n") for line in open("input")]
# input = [line.rstrip("\n") for line in open("test")]
xmas = 0
for row in range(len(input)):
    for col in range(len(input[0])):
        if input[row][col] == "X":
            for d in ((-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)):
                xmas += find(input, row, col, d, "XMAS")

print(xmas)

x_mas = 0
for row in range(1, len(input) - 1):
    for col in range(1, len(input[0]) - 1):
        if input[row][col] == "A":
            if list(sorted([input[row - 1][col - 1], input[row+1][col+1]])) == ["M", "S"] and list(sorted([input[row - 1][col + 1], input[row+1][col-1]])) == ["M", "S"]:
                x_mas += 1

print(x_mas)