# Initially there are n towers.
# Each tower is of height m
def towerBreakers(n, m):
    # Towers have a height of 1, P1 can't do anything and loses
    if m == 1:
        return 2
    # There is only 1 tower, P1 does the most optimal move and wins,
    # P2 can't do anything and loses
    if n == 1:
        return 1
    if n % 2 == 0:
        # P2 mimics every single move that P1 does. This results in P2
        # always having the last move, meaning that P1 will always lose.
        return 2
    # P1 takes down 1 tower, effectively making it so that there are an even
    # number of playable towers. Now, P1 mimics everything P2 does, resulting
    # in P1 always having the last move, meaning that P2 will always lose.
    return 1
