#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    energy = 100
    current_cloud = 0

    energy -= 1
    current_cloud = (current_cloud + k) % len(c)
    if c[current_cloud] == 1:
        energy -= 2
    while energy > 0 and current_cloud != 0:
        energy -= 1
        current_cloud = (current_cloud + k) % len(c)
        if c[current_cloud] == 1:
            energy -= 2

    if energy < 0:
        energy = 0
    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
