def saveThePrisoner(n, m, s):
    move = m % n
    position = s + move - 1
    position %= n
    if position == 0:
        position = n
    return position
