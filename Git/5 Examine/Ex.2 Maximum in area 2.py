n = int(input())
mtx = [[int(i) for i in input().split()] for _ in range(n)]

mx = 0
for i in range(n):
    for j in range(n):
        if mtx[i][j] > mx and (i > n-1-j or i+j+1 == n):
            mx = mtx[i][j]
print(mx)
