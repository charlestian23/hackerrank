cases = int(input())
for i in range(cases):
	input()
	set1 = set(map(int, input().split()))
	input()
	set2 = set(map(int, input().split()))
	print(set1.issubset(set2))