n = int(input())
mtx = [[int(i) for i in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i<j:
            mtx[i][j], mtx[j][i] =mtx[j][i] ,mtx[i][j]
        else:
            continue
    print(*mtx[i])