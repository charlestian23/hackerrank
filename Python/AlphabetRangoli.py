def print_rangoli(size):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    length = size * 2 - 1
    length += length - 1
    lines = []
    previous = ""
    current = alphabet[size - 1]
    for i in range(size - 1, -1, -1):
        s = previous + current + previous[::-1]
        lines.append(s.center(length, "-"))
        previous += current + "-"
        current = alphabet[i-1]
    for s in lines:
        print(s)
    lines.pop()
    lines.reverse()
    for s in lines:
        print(s)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)