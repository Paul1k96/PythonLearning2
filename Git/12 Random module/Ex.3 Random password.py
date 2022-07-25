import random

length = int(input())    # длина пароля

for i in range(length):
    print(chr([random.randrange(65, 89), random.randrange(97, 122)][random.randint(0,1)]), end='')
    