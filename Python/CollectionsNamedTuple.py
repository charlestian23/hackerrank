from collections import namedtuple
lines = int(input())
total = 0
parameters = input().split()
for i in range(lines):
	student = namedtuple("Student", parameters)
	input1, input2, input3, input4 = input().split()
	s = student(input1, input2, input3, input4)
	total += int(s.MARKS)
print("{:.2f}".format(total / lines))