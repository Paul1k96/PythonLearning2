dic = {}
for _ in range(int(input())):
    tmp = tuple(input().split())
    dic[tmp[0]] = tmp[1:]

for _ in range(int(input())):
    tmp = input()
    for key in dic:
        if tmp in dic[key]:
            print(key)
