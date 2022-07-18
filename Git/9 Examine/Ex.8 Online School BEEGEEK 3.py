n = (int(input()), int(input()))
math = {input() for _ in range(n[0])}
inform = {input() for _ in range(n[1])}
only_one = len(math ^ inform)
if only_one > 0:
    print(only_one)
else:
    print('NO')
