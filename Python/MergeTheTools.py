def merge_the_tools(string, k):
    substrings = [string[i:i+k] for i in range(0, len(string), k)]
    for t in substrings:
        letters = set()
        subsequence = ""
        for letter in t:
            if letter not in letters:
                subsequence += letter
                letters.add(letter)
        print(subsequence)

if __name__ == '__main__':
    # string, k = input(), int(input())
    string = "AABCAAADA"
    k = 3
    merge_the_tools(string, k)