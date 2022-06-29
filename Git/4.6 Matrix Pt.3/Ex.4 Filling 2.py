rc, count = [int(i) for i in input().split()], 0
mtx = []
for i in range(rc[0]):
    mtx += [[]]
    count = i+1
    for j in range(rc[1]):
        mtx[i] += [count]
        count += rc[0]
        print(str(mtx[i][j]).ljust(3), end='')
    print()