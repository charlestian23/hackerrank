from itertools import permutations
string, length = input().split()
print(*["".join(x) for x in permutations(sorted(string), int(length))], sep="\n")