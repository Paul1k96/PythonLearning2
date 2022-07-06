n = int(input())
mtx = [[int(i) for i in input().split()] for _ in range(n)]
sample = [i for i in range(1, n+1)]

flag = True
for i in range(n):
    sort_list1, sort_list2 = [], []

    for j in range(n):
        sort_list1 += [mtx[i][j]]
        sort_list2 += [mtx[j][i]]

    sort_list1.sort()
    sort_list2.sort()

    if sort_list1 != sample or sort_list2 != sample:
        flag = False
        break

if flag == True:
    print('YES')
else:
    print('NO')
