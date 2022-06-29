rc, count = [int(i) for i in input().split()], 0
mtx = []
for i in range(rc[0]):
    mtx += [[]]
    for j in range(rc[1]):
        count+=1
        mtx[i] += [count]
        print(str(mtx[i][j]).ljust(3), end='')
    print()