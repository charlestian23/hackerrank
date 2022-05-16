n = int(input())
temp = input().split()
lis = [int(s) for s in temp]
s = set(map(int, lis))
total = n * sum(s)
temp = sum(lis)
print(int((total - temp) / (n - 1)))