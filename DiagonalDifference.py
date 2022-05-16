def diagonalDifference(arr):
    d1 = 0
    d2 = 0
    index = 0
    for row in arr:
        d1 += row[index]
        d2 += row[-index - 1]
        index += 1
    return abs(d1 - d2)
