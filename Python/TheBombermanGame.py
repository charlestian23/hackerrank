#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    modified_grid = [[character for character in row] for row in grid]
    result = bomberman_helper(n, modified_grid)
    modified_result = []
    for row in result:
        string = ""
        for character in row:
            string += character
        modified_result.append(string)
    return modified_result


def bomberman_helper(n, grid):
    # In the first two seconds, nothing happens
    if n < 2:
        return grid
    # If an even number of seconds has passed, then the grid is full of bombs
    if n % 2 == 0:
        new_grid = ["O" * len(grid[0]) for i in range(len(grid))]
        return new_grid
    # Check if it is the 3rd second (or some multiple of 3 seconds)
    if (n - 1) % 4 != 0:
        return explode(grid)
    # Check if it is the 5th second (or some multiple of 5 seconds)
    return explode(explode(grid))


def explode(grid):
    print(grid)
    new_grid = [["O"] * len(grid[0]) for i in range(len(grid))]
    positions = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                positions.append((i, j))
    for i, j in positions:
        new_grid[i][j] = "."
        if i + 1 < len(new_grid):
            new_grid[i + 1][j] = "."
        if i - 1 >= 0:
            new_grid[i - 1][j] = "."
        if j + 1 < len(new_grid[0]):
            new_grid[i][j + 1] = "."
        if j - 1 >= 0:
            new_grid[i][j - 1] = "."
    return new_grid
