def gridChallenge(grid):
    # Write your code here
    new_grid = []
    for arr in grid:
        new_arr = [num for num in arr]
        new_arr.sort()
        new_grid.append(new_arr)
    flipped = [[new_grid[i][j] for i in range(len(new_grid))] for j in range(len(new_grid[0]))]
    for column in flipped:
        column_sorted = [num for num in column]
        column_sorted.sort()
        if column != column_sorted:
            return "NO"
    return "YES"
