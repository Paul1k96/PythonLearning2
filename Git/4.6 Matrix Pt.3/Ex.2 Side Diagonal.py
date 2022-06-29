n = int(input())
mtx = [[0]*n for _ in range(n)]
for i in range(n):
    mtx[i][n-i-1] = 1
    for j in range(n):
        if i > n-j-1:
            mtx[i][j] = 2
    print(*mtx[i])