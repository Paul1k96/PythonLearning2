txt = input().split()
result = {}
for i in range(len(txt)):
    if txt[i] in result:
        result[txt[i]] += 1
        txt[i] += '_' + str(result[txt[i]])
    else:
        result[txt[i]] = 0
print(*txt)