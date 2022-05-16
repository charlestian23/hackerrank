from calendar import day_name, weekday
temp = input().split()
lis = [int(s) for s in temp]
print(list(day_name)[weekday(lis[2], lis[0], lis[1])].upper())