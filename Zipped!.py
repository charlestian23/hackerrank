grades, lines = input().split()
grades = int(grades)
lines = int(lines)
lis = []
for i in range(lines):
	lis.append(list(map(float, input().split())))
for i in zip(*lis):
	print(sum(i)/len(i))