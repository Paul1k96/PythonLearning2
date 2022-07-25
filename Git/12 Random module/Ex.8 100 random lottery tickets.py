from random import randrange as r

for_check = []
i = 0
while i != 100:
    ticket = r(1000000, 10000000)
    if ticket in for_check:
        for_check += [ticket]
        continue
    else:
        print(ticket)
        i += 1
