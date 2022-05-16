#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    arr = [[] for i in range(n)]
    last_answer = 0
    result = []
    for query in queries:
        which_query = query[0]
        x = query[1]
        y = query[2]
        idx = (x ^ last_answer) % n
        if which_query == 1:
            arr[idx].append(y)
        elif which_query == 2:
            last_answer = arr[idx][y % len(arr[idx])]
            result.append(last_answer)
    return result
