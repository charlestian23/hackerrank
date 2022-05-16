if __name__ == '__main__':
    N = int(input())
	lis = []
	for i in range(N):
		temp = input().split()
		if temp[0] == "insert":
			lis.insert(int(temp[1]), int(temp[2]))
		elif temp[0] == "print":
			print(lis)
		elif temp[0] == "remove":
			lis.remove(int(temp[1]))
		elif temp[0] == "append":
			lis.append(int(temp[1]))
		elif temp[0] == "sort":
			lis.sort()
		elif temp[0] == "pop":
			lis.pop()
		elif temp[0] == "reverse":
			lis.reverse()