x, xtwo = input().split(), []
for i in range(len(x)):
    xtwo += [x[i-1]]
print(*xtwo)
