turns = input()
for i in range(int(turns)):
	lis = input().split()
	try:
		a = int(lis[0])
		b = int(lis[1])
		try:
			print(a // b)
		except ZeroDivisionError as e:
			print("Error Code:", e)
	except ValueError as e:
		print("Error Code:", e)