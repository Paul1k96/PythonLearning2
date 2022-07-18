n = int(input())
result = {input() for _ in range(int(input()))}
for _ in range(n-1):
    tmp = {input() for _ in range(int(input()))}
    result &= tmp
print(*sorted(result), sep='\n')

