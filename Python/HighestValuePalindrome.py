#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here

    # NOT DONE

    lis = list(s)
    lis_copy = list(s)
    count = k
    front = 0
    end = -1
    while front < end + n:
        if lis[front] != lis[end]:
            if count <= 0:
                return "-1"
            lis[front] = lis[end] = max(lis[front], lis[end])
            count -= 1
        front += 1
        end -= 1

    front = 0
    end = -1
    while count > 0 and front < end + n:
        if lis[front] != '9':
            if lis_copy[front] != lis_copy[end]:
                lis[front] = lis[end] = '9'
                count -= 1
            elif k > 1:
                lis[front] = lis[end] = '9'
                count -= 2
        front += 1
        end -= 1

    if count > 0 and n % 2 == 1:
        lis[n // 2] = '9'

    return "".join(lis)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
