def superDigit(n, k):
    p = int(n)
    if p < 10:
        return p
    total = 0
    while p != 0:
        total += p % 10
        p //= 10
    return superDigitHelper(total * k)


def superDigitHelper(p):
    if p < 10:
        return p
    total = 0
    while p != 0:
        total += p % 10
        p //= 10
    return superDigitHelper(total)
