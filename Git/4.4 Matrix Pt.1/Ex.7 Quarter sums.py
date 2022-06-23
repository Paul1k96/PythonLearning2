mtx = [list(map(int, input().split())) for _ in range(int(input()))]
n = len(mtx)
up,left,right,low = 0,0,0,0
for i in range(n):
    for j in range(len(mtx[i])):
        if i<j and i < n-1-j:
            up += mtx[i][j]
        if i>j and i < n-1-j:
            left += mtx[i][j]
        if i<j and i > n-1-j:
            right += mtx[i][j]
        if i>j and i > n-1-j:
            low += mtx[i][j]
print('Верхняя четверть:', up)
print('Правая четверть:', right)
print('Нижняя четверть:', low)
print('Левая четверть:', left)
