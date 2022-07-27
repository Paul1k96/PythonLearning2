# finds the largest regular irreducible fraction with the sum of the numerator and denominator equal to n
from fractions import Fraction

n = int(input())
result = 0
for i in range(n):
    for j in range(i):
        tmp = Fraction(j, i)
        if tmp >= result and tmp.numerator+tmp.denominator == n:
            result = tmp
print(result)
