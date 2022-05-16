from collections import defaultdict
a_len, b_len = input().split()
d = defaultdict(list)
for i in range(1, int(a_len) + 1):
	d[input()].append(i)
lis = list(d)
for i in range(int(b_len)):
	letter = input()
	if letter in lis:
		print(*d[letter])
	else:
		print(-1)