import random

n = int(input())    # количество попыток

for i in range(n):
    print(['Орел', 'Решка'][random.randrange(2)])