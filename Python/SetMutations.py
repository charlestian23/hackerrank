input()
set1 = set(map(int, input().split()))
commands = int(input())
for i in range(commands):
	lis = input().split()
	command = lis[0]
	set2 = set(map(int, input().split()))
	if command == "intersection_update":
		set1.intersection_update(set2)
	elif command == "symmetric_difference_update":
		set1.symmetric_difference_update(set2)
	elif command == "difference_update":
		set1.difference_update(set2)
	elif command == "update":
		set1.update(set2)
print(sum(set1))