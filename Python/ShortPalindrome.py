#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'shortPalindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def shortPalindrome(s):
    indices = dict()
    for i in range(len(s)):
        if s[i] not in indices:
            indices[s[i]] = []
        indices[s[i]].append(i)

def find_max_lower(list, index):
    for i in range(len(index)):
        if list[i] >= index:
            return i - 1
    return len(index) - 1

def find_min_upper(list, index):
    for i in range(len(index) - 1, -1, -1):
        if list[i] <= index:
            return i + 1
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = shortPalindrome(s)

    fptr.write(str(result) + '\n')

    fptr.close()
