#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# Median of medians method
def findMedian(arr):
    return selection(arr, math.floor(len(arr) / 2) + 1)


def selection(arr, k):
    v = random.choice(arr)
    s_left = []
    s_v = []
    s_right = []
    for num in arr:
        if num < v:
            s_left.append(num)
        elif num == v:
            s_v.append(num)
        else:
            s_right.append(num)
    print(s_left, s_v, s_right)
    if k <= len(s_left):
        return selection(s_left, k)
    elif len(s_left) < k <= len(s_left) + len(s_v):
        return v
    else:
        return selection(s_right, k - len(s_left) - len(s_v))


if __name__ == '__main__':
    input_string = "0 1 2 4 6 5 3"
    arr = list(map(int, input_string.rstrip().split()))
    print(findMedian(arr))
