set1 = set(map(int, input().split()))
cases = int(input())
passed = True
for i in range(cases):
	set2 = set(map(int, input().split()))
	if not set2.issubset(set1):
		passed = False
		break
print(passed)