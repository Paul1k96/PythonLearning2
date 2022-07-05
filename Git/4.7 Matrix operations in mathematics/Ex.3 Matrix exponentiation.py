n = int(input())
mtx = [[int(i) for i in input().split()] for _ in range(n)]
repeat = int(input())

def deep(mtx_fin):
    mx = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            mx[i][j] = mtx_fin[i][j]
    return mx

mtx_tmp = mtx
mtx_fin = [[0]*n for _ in range(n)]
for _ in range(repeat-1):
    for i in range(n):
        for j in range(n):
            calc = 0

            for p in range(n):
                calc += mtx_tmp[i][p] * mtx[p][j]

            mtx_fin[i][j] = calc
    mtx_tmp = deep(mtx_fin)

for i in mtx_fin:
    print(*i)
