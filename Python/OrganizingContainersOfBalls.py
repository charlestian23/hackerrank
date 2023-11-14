#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    empty_containers = 0
    for c in container:
        if sum(c) == 0:
            empty_containers += 1
    if len(container) - empty_containers != len(container[0]):
        return "Impossible"

    container_sizes = dict()
    for c in container:
        if sum(c) != 0:
            if sum(c) not in container_sizes:
                container_sizes[sum(c)] = 0
            container_sizes[sum(c)] += 1

    total_colors = [sum(row[i] for row in container) for i in range(len(container[0]))]

    for color in total_colors:
        if color not in container_sizes:
            return "Impossible"
        if container_sizes[color] == 0:
            return "Impossible"
        else:
            container_sizes[color] -= 1

    return "Possible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
