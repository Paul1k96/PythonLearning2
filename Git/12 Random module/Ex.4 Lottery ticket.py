import random

number = []
while len(number) != 7:
    rndnmb = random.randint(1, 49)
    if rndnmb in number:
        continue
    else:
        number += [rndnmb]

print(*sorted(number))