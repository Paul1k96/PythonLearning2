a = input() + input()
if [str(i) for i in range(10)] == sorted(set(a)):
    print('YES')
else:
    print('NO')
