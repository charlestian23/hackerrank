def sockMerchant(n, ar):
    # Write your code here
    d = dict()
    for num in ar:
        if num not in d:
            d[num] = 0
        d[num] += 1
    pairs = 0
    for key in d.keys():
        pairs += d[key] // 2
    return pairs
