from fractions import Fraction

res = 0
for i in range(int(input())):
    res += Fraction(1, (i+1)**2)
print(res)
