tmp_lst = []
for _ in range(int(input())):
    tmp = input().split(':')
    tmp_lst += [(tmp[0].lower(), tmp[1].strip(' '))]

dic_prog = dict(tmp_lst)

for _ in range(int(input())):
    print(dic_prog.get(input().lower(), 'Не найдено'))