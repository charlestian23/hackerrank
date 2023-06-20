#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    lis = sorted(x)
    index = 0
    count = 0
    while index < len(x):
        index = get_position_within_range(lis, k, index)
        count += 1
        index = get_position_within_range(lis, k, index)
        index += 1
    return count

def get_position_within_range(x, k, position):
    for i in range(position, len(x) - 1):
        if x[i + 1] > x[position] + k:
            return i
    return len(x) - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
0