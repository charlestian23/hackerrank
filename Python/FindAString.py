def count_substring(string, sub_string):
	counter = 0
	while string.count(sub_string) != 0:
		counter += 1
		string = string[string.index(sub_string) + 1:]
	return counter

if __name__ == '__main__':
	string = input().strip()
	sub_string = input().strip()

	count = count_substring(string, sub_string)
	print(count)