n = int(input())
lst = [int(input()) for i in range(n)]
product_number, flag = int(input()), False
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i]*lst[j]==product_number:
            flag = True
            break
if flag == True:
    print('ДА')
else:
    print('НЕТ')
