n, count = input(), 0
k = []
for i in range(1, len(n)+1):
    if count==3:
        k+=','
        count=0
    count += 1
    k+=n[-i]
print(*k[::-1], sep='')
