r, c = [int(i) for i in input().split()]
mtx = [[0]*c for _ in range(r)]

count = 0
for p in range(r*c):
    for i in range(r):
        for j in range(c):
            if p == i+j:
                count+=1
                mtx[i][j] = count

# вывод матрицы
for i in mtx:
    for j in i:
        print(str(j).ljust(3), end='')
    print()