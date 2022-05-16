from itertools import product
temp = input().split()
temp2 = input().split()
lis = [int(i) for i in temp]
lis2 = [int(i) for i in temp2]
products = list(product(lis, lis2))
for i in products:
	print(i, "", end="")