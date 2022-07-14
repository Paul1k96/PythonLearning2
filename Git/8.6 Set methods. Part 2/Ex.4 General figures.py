myset = set([int(i) for i in range(10)])
for _ in range(int(input())):
    myset &= set([int(i) for i in list(input())])
print(*sorted(myset))