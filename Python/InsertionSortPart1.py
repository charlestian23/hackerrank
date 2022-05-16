#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    counter = len(arr) - 1
    inserted = False
    e = arr[-1]
    while counter >= 0 and not inserted:
        if counter == 0 or arr[counter - 1] < e:
            arr[counter] = e
            inserted = True
        else:
            arr[counter] = arr[counter - 1]
        print(*arr)
        counter -= 1

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
