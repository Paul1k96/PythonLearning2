r, c = [int(i) for i in input().split()]
mtx = [[0]*c for _ in range(r)]

count, gl_count, flag = 1, 0, True
x,y = -1, 0
for p in range(r*c):

    if flag == True:
        if x != c-gl_count-1:
            x += 1
            mtx[y][x] = count
            count += 1

        elif y != r-gl_count-1:
            y += 1
            mtx[y][x] = count
            count += 1


        if x == c-gl_count-1 and y == r-gl_count-1:
            flag = False
            gl_count += 1
            # отладка
            # print(x, y, flag, gl_count, p, count)
            continue

    if flag == False :
        if x !=  gl_count-1:
            x -= 1
            mtx[y][x] = count
            count += 1

        elif y != gl_count:
            y -= 1
            mtx[y][x] = count
            count += 1

        if y == gl_count and x == gl_count-1:
            flag = True
    # отладка
    # print(x, y, flag, gl_count, p, count)

#вывод матрицы
for i in mtx:
    for j in i:
        print(str(j).ljust(3), end='')
    print()
