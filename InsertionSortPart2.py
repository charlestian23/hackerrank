#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        counter = 0
        inserted = False
        item = arr[i]
        arr.pop(i)
        for j in range(i):
            if item < arr[j] and not inserted:
                arr.insert(j, item)
                inserted = True
        if not inserted:
            arr.insert(i, item)
        print(*arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)