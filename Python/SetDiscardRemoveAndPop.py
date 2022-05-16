n = int(input())
s = set(map(int, input().split()))
n = int(input())
for i in range(n):
	lis = input().split()
	if lis[0] == "pop":
		s.pop()
	elif lis[0] == "remove":
		s.remove(int(lis[1]))
	elif lis[0] == "discard":
		s.discard(int(lis[1]))
print(sum(s))