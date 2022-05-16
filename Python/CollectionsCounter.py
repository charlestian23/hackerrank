from collections import Counter
input()
database = Counter([int(i) for i in input().split()])
orders = int(input())
profit = 0
for i in range(orders):
	size, price = input().split()
	size = int(size)
	price = int(price)
	if database[size] != 0:
		profit += price
		database[size] -= 1
print(profit)