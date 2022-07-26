import string
from random import choice, shuffle


def generate_password(length):
    exceptions = set('IloO')
    dig = tuple(set(string.digits[2:]))
    str_up = tuple(set(string.ascii_uppercase).difference(exceptions))
    str_low = tuple(set(string.ascii_lowercase).difference(exceptions))

    cnt = 0
    password = []
    while cnt != length:
        a, b, c = choice(dig), choice(str_up), choice(str_low)
        if cnt < 3:
            password += [a]
            cnt += 1
            password += [b]
            cnt += 1
            password += [c]
            cnt += 1
        else:
            password += choice([a, b, c])
            cnt += 1

    shuffle(password)
    password = ''.join(password)
    return password


def generate_passwords(count, length):
    out = []
    for i in range(count):
        out += [generate_password(length)]
    return out


n, m = int(input()), int(input())

print(*generate_passwords(n,m), sep='\n')
