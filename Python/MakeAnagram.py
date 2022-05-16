def makeAnagram(a, b):
    intersection_length = 0
    x = list(b)
    for c in a:
        if c in x:
            x.remove(c)
            intersection_length += 1
    return len(a) - intersection_length + len(b) - intersection_length
