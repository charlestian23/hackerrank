def lonelyinteger(a):
    dictionary = dict()
    for num in a:
        if num not in dictionary:
            dictionary[num] = 0
        dictionary[num] += 1
    for num in dictionary.keys():
        if dictionary[num] == 1:
            return num
    return None
