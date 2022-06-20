def pascal(n):
    list1 = [[int(1)]*(i+1) for i in range(n+1)] #создание списка из списков
    for j in range(2,len(list1)):

        a = list1[j]      # присваиваем список по индексу j=>3
        b = list1[j-1]    # присваеваем список перед a

        for k in range(1,len(a)-1):  # цикл для обработки списка a, не затрагивая границы из единиц по бокам

            a[k] = b[k-1]+b[k]       # сумма чисел
        list1[j] = a                 # интегрирование списка a вместо списка list[j]

    return list1              # возвращаем последний список

pasc = pascal(int(input()))
for p in range(len(pasc)-1):
    print(*pasc[p])