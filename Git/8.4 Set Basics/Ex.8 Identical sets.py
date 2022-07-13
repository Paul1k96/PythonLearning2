a, b, c = input().split()
if set(a) == set(b) and set(b) == set(c):
    print('YES')
else:
    print('NO')