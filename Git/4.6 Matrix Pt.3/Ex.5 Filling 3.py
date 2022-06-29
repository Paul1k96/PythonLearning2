n = int(input())
mtx = [[0]*n for _ in range(n)]
for i in range(n):
    mtx[i][i] = 1
    mtx[i][n-i-1] = 1
    print(*mtx[i])