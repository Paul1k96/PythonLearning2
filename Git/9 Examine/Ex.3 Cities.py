lst = [input() for _ in range(int(input())+1)]
cit = set(lst)
if len(lst) == len(cit):
    print('OK')
else:
    print('REPEAT')