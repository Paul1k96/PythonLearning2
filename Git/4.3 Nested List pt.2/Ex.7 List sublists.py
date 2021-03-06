# пример a b v
def sublist(txt):
    total = [[]]
    n = len(txt)
    count, count_total = 0, 0

    for i in range(n):                 # цикл для деления задачи на кол-во типов списков по длине. Прим.: всего 3 типа списка (1 симв, 2 симв и 3 симв)
        count += 1                     # счётчик для кол-ва символов в одном списке каждого типа
        anticount, txt_count = n-i, 0  # обратный счётчик для кол-ва списков каждого отдельного типа и счётчик для исходного текста
        #print (count, anticount)      # отладка счётчиков

        for _ in range(anticount):     # цикл с кол-вом списков по типу n
            total += [[]]              # добавление пустого списка
            count_total += 1           # счётчик для финального списка

            for _ in range(count):                   # цикл для заполнения финального списка.
                total[count_total] += txt[txt_count] # заполнение текущего типа списка символами из исходного текста
                if txt_count == n-1:                 # условие, что-бы не выходить за рамки счётчика текста
                    txt_count = 0
                else:                                # движение счётчика для перемещения по исходному тексту
                    txt_count += 1

            txt_count = txt_count-(count-1)          # изменение счётчика для того, что бы он перемещался на 1 символ вправо. Прим.: [a,b], [b,v]

    return total

print(sublist(input().split()))