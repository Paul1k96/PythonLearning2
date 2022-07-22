dic = {1:  ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
       2:  ['D', 'G'],
       3:  ['B', 'C', 'M', 'P'],
       4:  ['F', 'H', 'V', 'W', 'Y'],
       5:  ['K'],
       8:  ['J', 'X'],
       10: ['Q', 'Z']}

sm = 0
for i in list(input()):
    for key in dic:
        if i in dic[key]:
            sm += key
print(sm)
