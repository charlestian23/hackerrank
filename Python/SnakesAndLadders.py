#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#

def quickestWayUp(ladders, snakes):
    graph = dict()
    for item in ladders:
        graph[item[0]] = [item[1]]
    for item in snakes:
        graph[item[0]] = [item[1]]
    heads = [item[0] for item in ladders] + [item[0] for item in snakes]
    for i in range(1, 101):
        if i not in graph:
            neighbors = [i + j for j in range(1, 7) if i + j <= 100]
            graph[i] = neighbors

    # Dijkstra's algorithm, used to find shortest path to point
    unvisited_nodes = [i for i in range(1, 101)]
    shortest_path = dict()
    for i in range(1, 101):
        shortest_path[i] = 500
    shortest_path[1] = 0

    while len(unvisited_nodes) != 0:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbors = graph[current_min_node]
        for neighbor in neighbors:
            add_amount = 1
            if current_min_node in heads:
                add_amount = 0
            new_distance = shortest_path[current_min_node] + add_amount
            if new_distance < shortest_path[neighbor]:
                shortest_path[neighbor] = new_distance

        unvisited_nodes.remove(current_min_node)

    if shortest_path[100] == 500:
        return -1
    return shortest_path[100]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
