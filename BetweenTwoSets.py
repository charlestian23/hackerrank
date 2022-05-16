#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    highest = b[0]
    lis = [i+1 for i in range(highest)]
    numbers = lis.copy()
    for i in lis:
        for x in a:
            if i % x != 0 and i in numbers:
                numbers.remove(i)
    passed = numbers.copy()
    for y in b:
        for n in numbers:
            if y % n != 0 and n in passed:
                passed.remove(n)
    return len(passed)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
