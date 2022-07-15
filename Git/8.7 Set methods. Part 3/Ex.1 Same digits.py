myset1, myset2 = set(input()), set(input())
if  myset1.isdisjoint(myset2):
    print('NO')
else:
    print('YES')