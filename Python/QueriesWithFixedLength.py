#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def solve(arr, queries):
    result = []
    for query in queries:
        if query == len(arr):
            result.append(max(arr))
            continue
        smallest_max = -1
        index = 0
        while index < len(arr) - query + 1:
            sub_list = arr[index:index + query]
            local_max = max(sub_list)
            local_index = sub_list.index(local_max)
            if smallest_max == -1 or local_max < smallest_max:
                smallest_max = local_max
            index += local_index + 1
        result.append(smallest_max)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
