# int s[n]: the numbers on each of the squares of chocolate
# int d: Ron's birth day
# int m: Ron's birth month
# Note subarray != subsequence
def birthday(s, d, m):
    combos = set()
    for i in range(len(s) - m + 1):
        current = s[i:i+m]
        if sum(current) == d:
            combos.add(tuple(current))
    return len(combos)


if __name__ == '__main__':
    print(birthday([4], 4, 1))
