#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) % 2 == 1:
        return -1
    middle = int(len(s) / 2)
    front = s[:middle]
    back = s[middle:]
    front_dict = dict()
    back_dict = dict()
    for letter in front:
        if letter not in front_dict:
            front_dict[letter] = 0
        front_dict[letter] += 1
    for letter in back:
        if letter not in back_dict:
            back_dict[letter] = 0
        back_dict[letter] += 1

    for letter in front:
        if letter in back:
            while front_dict[letter] > 0 and back_dict[letter] > 0:
                front_dict[letter] -= 1
                back_dict[letter] -= 1

    total = 0
    for letter in back_dict:
        total += back_dict[letter]
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
