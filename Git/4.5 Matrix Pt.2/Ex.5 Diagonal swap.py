r = int(input())
mtx = [input().split() for _ in range(r)]
for i in range(r):
    for j in range(r):

        if i == r-1-j  and i < j:
            mtx[i][i], mtx[j][i] = mtx[j][i], mtx[i][i]

        if r-i-1 == j and i < j:
            mtx[i][j], mtx[j][j] = mtx[j][j], mtx[i][j]

    print(*mtx[i])