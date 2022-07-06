r1, c1 = [int(i) for i in input().split()]
mtx1 = [[int(i) for i in input().split()] for _ in range(r1)]

input()

r2, c2 = [int(i) for i in input().split()]
mtx2 = [[int(i) for i in input().split()] for _ in range(r2)]

mtx = [[0]*r1 for _ in range(c2)]

for i in range(r1):
    for j in range(c2):
        calc = 0

        for p in range(r2):
            calc += mtx1[i][p] * mtx2[p][j]

        mtx[i][j] = calc
    print(*mtx[i])
