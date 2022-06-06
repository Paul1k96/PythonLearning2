n1,n2, k = list(range(1, int(input())+1)),[], int(input())
count=0
while len(n1)>1:
    if k == 1:
        n1 = [n1[-1]]
        break
    for i in range(len(n1)):
        count+=1
        if count%k!=0:
            n2.append(n1[i])
    n1 = n2
    n2 = []
print(*str(n1[0]), sep = '')