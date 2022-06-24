m1,m2 = int(input()),int(input())
for i in range(m1):
    for j in range(m2):
        print(str(i*j).ljust(3), end='')
    print()