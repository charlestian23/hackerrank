def matchingStrings(strings, queries):
    dictionary = dict()
    for string in strings:
        if string not in dictionary:
            dictionary[string] = 0
        dictionary[string] += 1
    result = []
    for query in queries:
        if query not in dictionary:
            result.append(0)
        else:
            result.append(dictionary[query])
    return result
