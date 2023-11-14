#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    sorted_prices = sorted(price)
    indices = dict()
    for i in range(len(price)):
        if price[i] not in indices:
            indices[price[i]] = []
        indices[price[i]].append(i)

    minimum_loss = -1
    for i in range(1, len(sorted_prices)):
        loss = sorted_prices[i] - sorted_prices[i - 1]
        if min(indices[sorted_prices[i]]) < max(indices[sorted_prices[i - 1]]) and (minimum_loss == -1 or minimum_loss > loss):
            minimum_loss = loss
    return minimum_loss


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
