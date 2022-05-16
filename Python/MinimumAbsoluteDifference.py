def minimumAbsoluteDifference(arr):
    sorted_arr = [i for i in arr]
    sorted_arr.sort()
    minimum = abs(arr[0] - arr[1])
    for i in range(1, len(sorted_arr) - 1):
        if minimum > abs(sorted_arr[i] - sorted_arr[i + 1]):
            minimum = abs(sorted_arr[i] - sorted_arr[i + 1])
    return minimum
