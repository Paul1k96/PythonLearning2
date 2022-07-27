from fractions import Fraction

x, y = input(), input()

print(x, '+', y, '=', Fraction(x)+Fraction(y))
print(x, '-', y, '=', Fraction(x)-Fraction(y))
print(x, '*', y, '=', Fraction(x)*Fraction(y))
print(x, '/', y, '=', Fraction(x)/Fraction(y))
