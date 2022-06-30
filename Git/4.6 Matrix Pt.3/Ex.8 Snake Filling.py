r, c = [int(i) for i in input().split()]
mtx, count = [], 0

for i in range(r):
    mtx += [[]]
    for j in range(c):
        count += 1
        mtx[i] += [count]
    if i % 2:
        mtx[i].reverse()

for i in mtx:
    for j in i:
        print(str(j).ljust(3), end='')
    print()
