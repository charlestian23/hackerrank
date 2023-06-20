#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    letters = dict()
    for letter in s:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1
    one_odd_allowed = True
    for letter in letters:
        if letters[letter] % 2 == 1 and not one_odd_allowed:
            return "NO"
        if letters[letter] % 2 == 1 and one_odd_allowed:
            one_odd_allowed = False
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
