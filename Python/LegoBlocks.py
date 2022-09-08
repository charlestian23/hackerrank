#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    mod = 1000000007
    # The number of combinations to build a single row
    # for m = 0 to 3
    combinations = [1, 1, 2, 4]
    # Each row is independent so the total combinations is the number of combinations for one row power 'n'
    total = [1, 1, 2 ** n, 4 ** n]
    # For m > 3, the total combinations is the sum of the combinations for the last 4 widths
    # Total combination for m - 1 by adding block width 1
    # Total combination for m - 2 by adding block width 2
    # Total combination for m - 3 by adding block width 3
    while len(combinations) <= m:
        c = sum(combinations[-4:]) % mod
        combinations.append(c) # possible combinations for just one row
        total.append(pow(c, n, mod)) # possible combinations for 'n' rows
    # To find the number of unstable combinations in a wall size i,
    # we progressively split the wall into two parts, j and (i-j).
    # (the wall is unstable if it can be divided to two or more parts)
    # The total unstable combinations for wall size i is the sum of all
    # the stable combinations for size j, multiply by the total combinations
    # (stable and unstable) for size i-j for each j=1 to i-1.
    # For i = 1, the stable combination = 1.
    stable = [0, 1]
    for i in range(2, m+1):
        # unstable[i] = sum((stable[j]*total[i-j]) for j in range(1,i))
        # stable[i] = total[i] - unstable[i]
        stable.append(total[i] - sum((stable[j]*total[i-j]) for j in range(1, i)) % mod)
    return stable[m] % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
