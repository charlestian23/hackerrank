def superDigit(n, k):
    if len(n) == 1 and k == 1:
        return int(n)

    total = 0
    for num in n:
        total += int(num)
    return superDigit(str(total * k), 1)
