#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    letter_count = dict()
    for letter in s:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    results = []
    for letter in letter_count:
        results.append((letter_count[letter], letter))
    results.sort(key=lambda x: (-x[0], ord(x[1])))
    for i in range(3):
        print(results[i][1], results[i][0])
