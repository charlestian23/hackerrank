cases = int(input())
for i in range(cases):
    number = input()
    if number.isdigit() and (number[0] == "7" or number[0] == "8" or number[0] == "9") and len(number) == 10:
        print("YES")
    else:
        print("NO")