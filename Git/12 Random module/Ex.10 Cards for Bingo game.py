from random import randrange as rnd
mtx = [[0]*5 for _ in range(5)]
full_numb = [i for i in range(1, 76)]
ln = len(mtx)
for i in range(ln):
    for j in range(ln):

        if not(i == j and i+j+1 == ln):
            tmp = full_numb.pop(rnd(len(full_numb)))
            mtx[i][j] = tmp
            print(str(mtx[i][j]).ljust(3), end='')

        else:
            print(str(mtx[i][j]).ljust(3), end='')
            continue

    print()




