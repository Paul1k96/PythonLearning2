r, c = int(input()), int(input())
mtx = [list(map(int, input().split())) for _ in range(r)]
swap = list(map(int, input().split()))
for i in range(r):
    mtx[i][swap[0]], mtx[i][swap[1]] = mtx[i][swap[1]], mtx[i][swap[0]]
    print(*mtx[i])