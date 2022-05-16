def counterGame(n):
    # Write your code here
    return helper(n, 0)


def helper(n, moves_made):
    power = 0
    while 2 ** power < n:
        power += 1
    if 2 ** power == n:
        if (moves_made + power) % 2 == 0:
            return "Richard"
        return "Louise"
    return helper(n - 2 ** (power - 1), moves_made + 1)
