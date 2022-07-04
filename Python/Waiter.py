#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def first_n_primes(n):
    primes = [2]
    number = 3
    while len(primes) != n:
        is_prime = True
        for prime in primes:
            if number % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
        number += 1
    return primes


def waiter(number, q):
    # Write your code here
    primes = first_n_primes(q)
    answers = []
    previous_a = [num for num in number]
    previous_b = []
    for i in range(q):
        a = []
        b = []
        for num in previous_a[::-1]:
            if num % primes[i] == 0:
                b.append(num)
            else:
                a.append(num)
        answers.extend(b[::-1])
        previous_a = a
        previous_b = b
    answers.extend(previous_a[::-1])
    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
