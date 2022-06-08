x, xtwo = input().split(), []
for i in range(1,len(x),2):
    tmp=[x[i]]+[x[i-1]]
    xtwo+=tmp
if len(x)%2!=0:
    xtwo.append(x[-1])
print(*xtwo)