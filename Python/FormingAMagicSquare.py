#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    magic1 = [[8, 3, 4],
              [1, 5, 9],
              [6, 7, 2]]
    magic2 = [[6, 1, 8],
              [7, 5, 3],
              [2, 9, 4]]
    magic3 = [[2, 7, 6],
              [9, 5, 1],
              [4, 3, 8]]
    magic4 = [[4, 9, 2],
              [3, 5, 7],
              [8, 1, 6]]
    min_cost1 = min(find_cost(s, magic1), find_cost(s, magic2), find_cost(s, magic3), find_cost(s, magic4))

    magic1.reverse()
    magic2.reverse()
    magic3.reverse()
    magic4.reverse()

    min_cost2 = min(find_cost(s, magic1), find_cost(s, magic2), find_cost(s, magic3), find_cost(s, magic4))

    return min(min_cost1, min_cost2)

def find_cost(matrix, magic_square):
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(magic_square[i][j] - matrix[i][j])
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
