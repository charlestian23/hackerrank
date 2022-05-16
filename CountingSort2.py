def countingSort(arr):
    result = [0] * (max(arr) + 1)
    for num in arr:
        result[num] += 1
    return_arr = []
    for i in range(len(result)):
        return_arr += [i] * result[i]
    return return_arr
