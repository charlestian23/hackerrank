def miniMaxSum(arr):
    arr_copy = [num for num in arr]
    arr_copy.sort()
    print(sum(arr_copy[:4]), sum(arr_copy[1:]))
