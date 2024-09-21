from itertools import product

k, m = input().split()
k = int(k)
m = int(m)
lists = []
for i in range(k):
    raw_line = input().split()
    lis = [int(x) for x in raw_line[1:]]
    lists.append(lis)

answer = 0
for value in product(*lists):
    total = sum(x ** 2 for x in value) % m
    answer = max(answer, total)
print(answer)
