n = int(input())
mtx = [['.']*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or i+j+1 == n or j == n//2 or i == n//2:
            mtx[i][j] = '*'
    print(*mtx[i])