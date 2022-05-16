import math


def sumXor(n):
    # Write your code here
    if n == 0:
        return 1
    binary = list(str(bin(n)))[2:]
    print(binary)
    return int(math.pow(2, binary.count('0')))
