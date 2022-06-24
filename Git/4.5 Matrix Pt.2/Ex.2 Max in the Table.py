r, c = int(input()), int(input())
mtx = [list(map(int, input().split())) for _ in range(r)]
mx = -10**9
for i in range(r):
    for j in range(c):
        if mtx[i][j] > mx:
            mx = mtx[i][j]
            coord = str(i)+' '+str(j)
print(coord)