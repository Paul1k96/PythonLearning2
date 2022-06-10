n = int(input())
lst, toxa, spisok, cnt = [input() for i in range(n)], 'anton', [], 0
for i in lst:
    cnt+=1
    tmp = str()
    cnt1 = 0
    for j in range(len(i)):
        a = i[j]
        if toxa == tmp:
            continue
        if a == toxa[cnt1]:
            tmp+=a
            cnt1+=1
    if toxa in tmp:
        spisok += [cnt]
print(*spisok)