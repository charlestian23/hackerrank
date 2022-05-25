def isValid(s):
    # Write your code here
    character_occurrences = dict()
    for character in s:
        if character not in character_occurrences:
            character_occurrences[character] = 0
        character_occurrences[character] += 1
    occurrences_occurrences = dict()
    for character in character_occurrences:
        occurrence = character_occurrences[character]
        if occurrence not in occurrences_occurrences:
            occurrences_occurrences[occurrence] = 0
        occurrences_occurrences[occurrence] += 1
    if len(occurrences_occurrences) > 2:
        return "NO"
    if len(occurrences_occurrences) < 2:
        return "YES"

    keys = list(occurrences_occurrences.keys())
    occurrences = [occurrences_occurrences[key] for key in keys]
    if not (occurrences[0] == 1 or occurrences[1] == 1):
        return "NO"
    if abs(keys[0] - keys[1]) == 1:
        return "YES"
    if (keys[0] == 1 and occurrences[0] == 1) or (keys[1] == 1 and occurrences[1] == 1):
        return "YES"
    return "NO"
