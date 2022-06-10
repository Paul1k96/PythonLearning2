inp, cnt1, cnt2 = input(), 0, 0
for i in range(len(inp)):
    if inp[i]=='Р':
        cnt1+=1
        if cnt1>cnt2:
            cnt2=cnt1
    else:
        cnt1=0
print(cnt2)

#s = input().split('О')
#print(len(max(s)))