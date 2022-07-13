a = input().split()
b = set()
for i in range(len(a)):
    for j in a[i]:
        if j in '-!?,.:;':
            a[i] = a[i].replace(j, "")
    b.add(a[i].lower())
print(len(b))