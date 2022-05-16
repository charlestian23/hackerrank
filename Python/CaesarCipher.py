def caesarCipher(s, k):
    # Write your code here
    lowercase = list("abcdefghijklmnopqrstuvwxyz")
    uppercase = list("abcdefghijklmnopqrstuvwxyz".upper())
    new_word = ""
    for letter in s:
        if letter in lowercase:
            new_index = lowercase.index(letter) + k
            if new_index >= len(lowercase):
                new_index %= len(lowercase)
            new_word += lowercase[new_index]
        elif letter in uppercase:
            new_index = uppercase.index(letter) + k
            if new_index >= len(uppercase):
                new_index %= len(lowercase)
            new_word += uppercase[new_index]
        else:
            new_word += letter
    return new_word
