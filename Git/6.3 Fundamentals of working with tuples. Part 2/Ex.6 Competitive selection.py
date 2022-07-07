n = int(input())
lst = [input() for _ in range(n)]
for i in lst:
    print(i)
print()
for i in lst:
    if i[-1] == '4' or i[-1] == '5':
        print(i)