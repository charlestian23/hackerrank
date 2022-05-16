def flippingBits(n):
    binary = list(bin(n))[2:]
    binary = ['0'] * (32 - len(binary)) + binary
    flipped = [1 if x == '0' else 0 for x in binary]
    flipped.reverse()
    value = 0
    for i in range(len(flipped)):
        value += flipped[i] * 2 ** i
    return value

if __name__ == '__main__':
    flippingBits(2147483647)
    