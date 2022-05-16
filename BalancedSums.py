def balancedSums(arr):
    # Write your code here
    current = arr[0]
    left_sum = 0
    right_sum = sum(arr[1:])
    for i in range(1, len(arr)):
        if left_sum == right_sum:
            return "YES"
        left_sum += current
        current = arr[i]
        right_sum -= current
    if left_sum == right_sum:
        return "YES"
    return "NO"
