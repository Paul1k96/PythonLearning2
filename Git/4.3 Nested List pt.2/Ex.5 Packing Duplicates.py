txt  = ''.join(input().split())
lst = [[txt[0]]]
count = 0

for i in range(1, len(txt)):
    if lst[count][0] == txt[i]:
        lst[count] += txt[i]
    else:
        lst+= [[txt[i]]]
        count+=1

print(lst)