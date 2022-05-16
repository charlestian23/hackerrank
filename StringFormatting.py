def print_formatted(number):
    length = len(str(bin(number))[2:]) + 1
    for i in range(1, number+1):
        decimal = "{number:{width}d}".format(number=i, width=length-1)
        octal = "{number:>{width}}".format(number=oct(i)[2:], width=length)
        hexidecimal = "{number:>{width}}".format(number=hex(i)[2:].upper(), width=length)
        binary = "{number:>{width}}".format(number=bin(i)[2:].upper(), width=length)
        print(decimal + octal + hexidecimal + binary)

if __name__ == '__main__':
    # n = int(input())
    print_formatted(17)