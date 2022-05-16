from itertools import combinations
string, length = input().split()
for i in range(1, int(length) + 1):
	print(*["".join(x) for x in combinations(sorted(string), i)], sep="\n")