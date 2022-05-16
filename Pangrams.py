def pangrams(s):
    # Write your code here
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in alphabet:
        if letter not in s.lower():
            return "not pangram"
    return "pangram"
