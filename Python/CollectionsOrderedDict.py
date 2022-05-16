from collections import OrderedDict
d = OrderedDict()
for i in range(int(input())):
	lis = input().split()
	item = ""
	for s in lis:
		if s.isalpha():
			item += s + " "
	if item not in d:
		d[item] = int(lis[-1])
	else:
		d[item] += int(lis[-1])
items = list(d)
for i in items:
	print(i, d[i], sep="")