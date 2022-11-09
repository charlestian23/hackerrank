#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

import heapq

def is_passed(k, pq):
    minimum = heapq.heappop(pq)
    if minimum >= k:
        return True
    heapq.heappush(pq, minimum)
    return False

def cookies(k, A):
    count = 0
    heapq.heapify(A)
    while not is_passed(k, A):
        first = heapq.heappop(A)
        try:
            second = heapq.heappop(A)
            heapq.heappush(A, first + 2 * second)
            count += 1
        except IndexError:
            if first < k:
                return -1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
