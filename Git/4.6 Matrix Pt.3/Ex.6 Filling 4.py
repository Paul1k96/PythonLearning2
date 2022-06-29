n = int(input())
mtx = [[0]*n for _ in range(n)]
for i in range(n):
    mtx[i][i] = 1
    mtx[i][n-i-1] = 1
    for j in range(n):
        if (i < j and i < n-j-1) or (i > j and i > n-j-1):
            mtx[i][j] = 1
    print(*mtx[i])