#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    less = []
    more = []
    equal = []
    pivot = arr[0]
    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            more.append(num)
        else:
            equal.append(num)
    less = quickSort(less)
    more = quickSort(more)
    return less + equal + more

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
