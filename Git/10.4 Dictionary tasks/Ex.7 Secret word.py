code = input()
code_dict = {}
for i in list(code):
    code_dict[i] = code_dict.get(i, 0) + 1

decode_dic = {}
for _ in range(int(input())):
    tmp = input().split(':')
    decode_dic[tmp[1].strip(' ')] = tmp[0]

for i in code:
    print(decode_dic[str(code_dict[i])], end='')
