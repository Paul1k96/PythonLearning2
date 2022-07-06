n = int(input())
sample = [i for i in range(n)]

mtx=[]
for i in range(n):
    mtx += [[]]
    count = i
    for j in range(n):
        mtx[i] += [count]
        if count > j-i:
            count -=1
        else:
            count +=1
    print(*mtx[i])

