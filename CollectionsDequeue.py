from collections import deque
d = deque()
for i in range(int(input())):
	lis = input().split()
	if lis[0] == "append":
		d.append(int(lis[1]))
	elif lis[0] == "appendleft":
		d.appendleft(int(lis[1]))
	elif lis[0] == "pop":
		d.pop()
	elif lis[0] == "popleft":
		d.popleft()
print(*d)