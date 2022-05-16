from itertools import combinations_with_replacement
string, length = input().split()
print(*["".join(x) for x in combinations_with_replacement(sorted(string), int(length))], sep="\n")