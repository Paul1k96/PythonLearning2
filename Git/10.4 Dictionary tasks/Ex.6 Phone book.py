dic = {}
for _ in range(int(input())):
    tmp = tuple(input().lower().split())
    if tmp[1] in dic:
        dic[tmp[1]] += [tmp[0]]
    else:
        dic[tmp[1]] = [tmp[0]]

for _ in range(int(input())):
    print(*dic.get(input().lower(), ['абонент не найден']))
