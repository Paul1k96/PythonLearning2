n = int(input())
mtx = [[int(i) for i in input().split()] for _ in range(n)]

flag = True
for i in range(n):
    for j in range(n):
        if i < n-1-j:
            if mtx[i][j] != mtx[n-j-1][n-i-1]:
                flag = False
                break
        else:
            continue

if flag == True:
    print('YES')
else:
    print('NO')