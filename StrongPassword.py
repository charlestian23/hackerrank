#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
	numbers = list("0123456789")
	lower_case = list("abcdefghijklmnopqrstuvwxyz")
	upper_case = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	special_characters = list("!@#$%^&*()-+")
	digits_needed = 0
	passed = False
	for i in numbers:
		if i in password:
			passed = True
			break
	if not passed:
		digits_needed += 1

	passed = False
	for c in lower_case:
		if c in password:
			passed = True
			break
	if not passed:
		digits_needed += 1

	passed = False
	for c in upper_case:
		if c in password:
			passed = T#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
	numbers = list("0123456789")
	lower_case = list("abcdefghijklmnopqrstuvwxyz")
	upper_case = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	special_characters = list("!@#$%^&*()-+")
	digits_needed = 0
	passed = False
	for i in numbers:
		if i in password:
			passed = True
			break
	if not passed:
		digits_needed += 1

	passed = False
	for c in lower_case:
		if c in password:
			passed = True
			break
	if not passed:
		digits_needed += 1

	passed = False
	for c in upper_case:
		if c in password:
			passed = True
			break
	if not passed:
		digits_needed += 1

	passed = False
	for c in special_characters:
		if c in password:
			passed = True
			break
	if not passed:
		digits_needed += 1

	if n + digits_needed < 6:
		digits_needed += 6 - n
	return digits_needed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
rue
			break
	if not passed:
		digits_needed += 1

	passed = False
	for c in special_characters:
		if c in password:
			passed = True
			break
	if not passed:
		digits_needed += 1

	if n + digits_needed < 6:
		digits_needed += n + 1
	return digits_needed

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
