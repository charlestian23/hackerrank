import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
	x = s[0].upper() + s[1:]
	for i in range(1, len(x)):
		if x[i - 1] == " " and x[i] != " ":
			x = x[:i] + x[i].upper() + x[i + 1:]
	return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
