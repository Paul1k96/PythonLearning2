x, count = input().split(), 1
for i in range(1,len(x)):
    if x[i-1]!=x[i]:
        count+=1
print(count)

