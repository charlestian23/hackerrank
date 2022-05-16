# PROBLEM: Given an array of integers, find the subset of non-adjacent elements with the maximum sum.
# Calculate the sum of that subset. It is possible that the maximum sum is 0, the case when all elements
# are negative.

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    max_sum = [0] * len(arr)
    max_sum[0] = max(0, arr[0])
    if len(arr) > 1:
        max_sum[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        max_sum[i] = max(max_sum[i - 2] + arr[i], max_sum[i - 1], arr[i])
    return max_sum[-1]

# Input: array of integers (arr)
# Output: integer representing maximum sum
# Recurrence:
#   Base cases: max(0, arr[0]) if i == 0, max(arr[0], arr[1]) if i == 1
#   max_sum[i] = max(max_sum[i - 2] + arr[i], max_sum[i - 1], arr[i]) for i > 1
# Running time: O(n)

