#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    nums = dict()
    result = 0
    for i in arr:
        if i not in nums:
            nums[i] = 0
        nums[i] += 1
        if i - d not in nums:
            nums[i - d] = 0
        if i - 2 * d not in nums:
            nums[i - 2 * d] = 0
        result += nums[i - d] * nums[i - 2 * d]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
