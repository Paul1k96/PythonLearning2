n = [int(input()), int(input())]
myset = {input() for _ in range(n[0])}
lst = [input() for _ in range(n[1])]
for i in lst:
    if i in myset:
        print('YES')
    else:
        print('NO')