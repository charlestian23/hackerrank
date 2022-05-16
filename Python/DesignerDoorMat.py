lis = input().split()
length = int(lis[0])
width = int(lis[1])
lis = []
pattern = ".|."
for i in range(length // 2):
	lis.append(pattern.center(width, "-"))
	pattern = ".|." + pattern + ".|."
for s in lis:
	print(s)
print("WELCOME".center(width, "-"))
lis.reverse()
for s in lis:
	print(s)