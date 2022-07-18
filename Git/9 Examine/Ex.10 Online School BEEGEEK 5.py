n = (int(input()), int(input()))
math_and_inform = [input() for _ in range(sum(n))]
myset1 = set()
myset2 = set()
for i in math_and_inform:
    if i not in myset1:
        myset1.add(i)
    else:
        myset2.add(i)
res = len(myset1)-len(myset2)
if res != 0:
    print(res)
else:
    print('NO')

