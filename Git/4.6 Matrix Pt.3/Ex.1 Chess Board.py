rc = [int(i) for i in input().split()]
mtx = [['.' for _ in range(rc[1])] for _ in range(rc[0])]
for i in range(rc[0]):
    for j in range(rc[1]):
        if (j+i+1)%2 == 0:
            mtx[i][j] = '*'
    print(*mtx[i])