from fractions import Fraction
from math import factorial
res = 0
for i in range(int(input())):
    res += Fraction(1, factorial(i+1))
print(res)
