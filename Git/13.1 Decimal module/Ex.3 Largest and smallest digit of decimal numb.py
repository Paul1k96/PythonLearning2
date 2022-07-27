from decimal import *
num = Decimal(input())
num_tuple = num.as_tuple()

if str(abs(num))[0] == str(num_tuple[0]*0):
    print(max(num_tuple[1]))
else:
    print(max(num_tuple[1])+min(num_tuple[1]))
