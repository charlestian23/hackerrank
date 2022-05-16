from operator import itemgetter
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    second_item = itemgetter(1)
    sort = sorted(records, key=second_item)
    names = []
    temp = sort[0][1]
    counter = 0
    while counter < len(sort) and temp == sort[counter][1]:
        counter += 1
    temp = sort[counter][1]
    while counter < len(sort) and temp == sort[counter][1]:
        names.append(sort[counter][0])
        counter += 1
    names.sort()
    for n in names:
        print(n)
