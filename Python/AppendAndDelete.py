# string s: the initial string
# string t: the desired string
# int k: the exact number of operations that must be performed
def appendAndDelete(s, t, k):
    start_common_letters = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            start_common_letters += 1
        else:
            break
    remove_from_s = len(s) - start_common_letters
    add_to_t = len(t) - start_common_letters
    minimum_operations = remove_from_s + add_to_t
    if k == minimum_operations:
        return "Yes"
    elif k < minimum_operations:
        return "No"
    else:
        remaining_operations = k - minimum_operations
        if remaining_operations % 2 == 0:
            return "Yes"
        elif remaining_operations >= 2 * start_common_letters:
            return "Yes"
        return "No"
