n = (int(input()), int(input()))
math = {input() for _ in range(n[0])}
inform = {input() for _ in range(n[1])}
print(len(math - inform))