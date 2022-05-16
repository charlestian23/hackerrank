def split_and_join(line):
    lis = line.split()
    string = ""
    for s in lis:
        string += s + "-"
    return string[:-1]

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)