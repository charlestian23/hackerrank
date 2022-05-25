#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    indices = dict()
    for i in range(len(arr)):
        if m - arr[i] in indices:
            return [indices[m - arr[i]], i + 1]
        indices[arr[i]] = i + 1
