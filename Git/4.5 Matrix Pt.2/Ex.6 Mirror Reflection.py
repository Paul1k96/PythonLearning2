n = int(input())
mtx = [input().split() for _ in range(n)]
for i in range(n//2):
    mtx[i], mtx[n-i-1] = mtx[n-i-1], mtx[i]
[print(*mtx[i]) for i in range(n)]