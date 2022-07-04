r, c = [int(i) for i in input().split()]
mtx1 = [[int(i) for i in input().split()] for _ in range(r)]
mtx2 = [[int(i) for i in input().split()] for _ in range(r+1)]
del mtx2[0]
for i in range(r):
    for j in range(c):
        mtx1[i][j] += mtx2[i][j]
    print(*mtx1[i])