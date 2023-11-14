#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    for i in range(1, len(s) - 1):
        if is_beautiful(int(s[:i]), s[i:]):
            print("YES", s[:i])
            return
    print("NO")

def is_beautiful(num, string):
    if len(string) == 0:
        return True

    next_value = num + 1
    if string.startswith(str(next_value)):
        new_string = string[len(str(next_value)):]
        return is_beautiful(next_value, new_string)
    return False

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
