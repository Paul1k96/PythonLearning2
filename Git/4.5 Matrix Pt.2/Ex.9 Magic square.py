n, flag = int(input()), True
mtx = [[int(i) for i in input().split()] for _ in range(n)]
mtx_rotate = []

# создание поворотной матрицы
for r in range(n):
    mtx_rotate += [[]]
    for c in range(n):
        mtx_rotate[r] += [mtx[n-c-1][r]]

# добавление к поворотной матрице диагоналей изначальной матрицы
mtx_rotate += [[]] + [[]]
for i in range(n):
    mtx_rotate[-1] += [mtx[i][i]]
    mtx_rotate[-2] += [mtx[i][n-i-1]]

# проверка на повторные числа в списке матрицы и прерывание, если повторное число и присваивание флагу False
for i in mtx_rotate:
    if flag == False:
        break

    for j in range(n):
        if flag == False :
            break
        if i[j] == 0:   # если ноль в матрице, то прерывание
            flag = False
            break

        for p in range(j):
            if i[j] == i[p]:
                flag = False
                break

# если флаг True, то проверка списков матрицы на равенство
if flag == True:
    for i in range(len(mtx_rotate)):
        mtx_rotate[i] = sum(mtx_rotate[i])
        if i>0:
            if mtx_rotate[i-1] != mtx_rotate[i]:
                flag = False
                break

if flag == True:
    print('YES')
else:
    print('NO')
