#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def maxSubarray(arr):
    return [maximum_subarray(arr), max_subsequence(arr)]


# Kadane's Algorithm
# References: https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
def maximum_subarray(array):
    max_so_far = min(array)
    max_ending_here = 0

    for num in array:
        max_ending_here += num
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


def max_subsequence(array):
    positive_nums = [num for num in array if num > 0]
    if len(positive_nums) == 0:
        return max(array)
    return sum(positive_nums)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
