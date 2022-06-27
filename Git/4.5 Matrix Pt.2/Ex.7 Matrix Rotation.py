n = int(input())
mtx = [input().split() for _ in range(n)]
mtx_rotated = []
for i in range(n):
    mtx_rotated += [[]]
    for j in range(n):
        mtx_rotated[i] += [mtx[n-j-1][i]]
    print(*mtx_rotated[i])