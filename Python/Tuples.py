if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    lis = []
    for i in integer_list:
        lis.append(i)
    print(hash(tuple(lis)))