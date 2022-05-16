import textwrap

def wrap(string, max_width):
    lis = textwrap.wrap(string, max_width)
	string = ""
	for s in lis:
		string += s + "\n"
	return string

f __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)