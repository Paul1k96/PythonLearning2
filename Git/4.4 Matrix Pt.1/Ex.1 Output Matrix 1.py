r, c = int(input()), int(input())
mrx = []
for i in range(r):
    mrx += [[]]
    for j in range(c):
        mrx[i]+= [input()]
        print(mrx[i][j], end=' ')
    print()