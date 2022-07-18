myset1 = {int(i) for i in input().split()}
myset2 = {int(i) for i in input().split()}
comb = myset1 & myset2
if len(comb) > 0:
    print(*sorted(comb, reverse=True))
else:
    print('BAD DAY')