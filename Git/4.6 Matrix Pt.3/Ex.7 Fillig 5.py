r, c = [int(i) for i in input().split()]
mtx = [[(i+j)%c+1 for j in range(c)] for i in range(r)]
for i in range(r):
    print(*mtx[i])