dic = {}
for i in input().split():
    dic[i] = dic.get(i, 0)+1
    print(dic[i], end=' ')
    