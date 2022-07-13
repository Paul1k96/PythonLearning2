lst = [int(i) for i in input().split()]
digset = set()
for i in lst:
    if i in digset:
        print('YES')
    else:
        print('NO')
        digset.add(i)