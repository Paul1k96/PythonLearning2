tmp = []
for _ in range(int(input())):
    tmp += [tuple(input().split())]

dic = dict(tmp)
word = input()

for key, value in dic.items():
    if word == key:
        print(value)
    if word == value:
        print(key)