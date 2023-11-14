#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    marked = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                marked.append((i, j))

    max_region_size = 0
    while len(marked) != 0:
        r, c = marked[0]
        visited = set()
        dfs(matrix, r, c, visited)
        for point in visited:
            marked.remove(point)
        if len(visited) > max_region_size:
            max_region_size = len(visited)
    return max_region_size

def dfs(matrix, row, column, visited):
    if row < 0 or column < 0 or row >= len(matrix) or column >= len(matrix[row]) or matrix[row][column] == 0:
        return

    if (row, column) not in visited:
        visited.add((row, column))
        dfs(matrix, row + 1, column, visited)
        dfs(matrix, row + 1, column + 1, visited)
        dfs(matrix, row, column + 1, visited)
        dfs(matrix, row - 1, column, visited)
        dfs(matrix, row, column - 1, visited)
        dfs(matrix, row - 1, column - 1, visited)
        dfs(matrix, row - 1, column + 1, visited)
        dfs(matrix, row + 1, column - 1, visited)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
