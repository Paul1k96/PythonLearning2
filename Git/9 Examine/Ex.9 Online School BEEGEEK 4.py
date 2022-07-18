myset1 = {i for i in input().split()}
myset2 = {i for i in input().split()}
print(*sorted(myset1 | myset2))
