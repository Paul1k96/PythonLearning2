n = int(input())
mtx = [list(map(int, input().split())) for _ in range(n)]
mtx_invert = []
for i in range(n):
    mtx_invert += [[]]
    for j in range(n):
        mtx_invert[i] += [mtx[j][i]]
if mtx == mtx_invert:
    print('YES')
else:
    print('NO')