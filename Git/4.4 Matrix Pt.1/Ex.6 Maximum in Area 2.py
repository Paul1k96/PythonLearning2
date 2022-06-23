mtx = [list(map(int, input().split())) for _ in range(int(input()))]
n = len(mtx)
mtx = [[mtx[i][j] for j in range(len(mtx[i])) if (i>j and i < n-1-j ) or j == i or (i < j and i > n-1-j) or i +j+1 == n] for i in range(n)]
mx = -100000000
for i in mtx:
    for j in range(len(i)):
        if i[j] > mx:
            mx = i[j]
print(mx)