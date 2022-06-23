mtx = [list(map(int, input().split())) for _ in range(int(input()))]
mtx = [[mtx[i][j] for j in range(len(mtx[i])) if i>j or j == i] for i in range(len(mtx))]
mx = -100000000
for i in mtx:
    for j in range(len(i)):
        if i[j] > mx:
            mx = i[j]
print(mx)