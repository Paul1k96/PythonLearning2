txt = input().split()
n = int(input())
mtx = []
for i in range(n):
    mtx += [txt[i::n]]
print(mtx)