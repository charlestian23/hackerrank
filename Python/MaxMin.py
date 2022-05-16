def maxMin(k, arr):
    # Write your code here
    lis = [num for num in arr]
    lis.sort()
    minimum_difference = lis[k - 1] - lis[0]
    for i in range(1, len(lis) - k + 1):
        if lis[k - 1 + i] - lis[i] < minimum_difference:
            minimum_difference = lis[k - 1 + i] - lis[i]
    return minimum_difference
