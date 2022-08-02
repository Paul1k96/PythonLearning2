from random import randrange
from math import tan, pi, radians


# REFERENCE FIGURE
n_ref = randrange(3, 8)
a_ref = randrange(2, 10)
s_ref = (n_ref*(a_ref**2))/(4*tan(radians(180)/n_ref))

# def draw_figure(side, angle):
#     pass

polygons = 0
while polygons != 25:
    n = randrange(3, 8)
    a = randrange(2, 10)
    print(n, a)
    s = (n * (a ** 2)) / (4 * tan(radians(180) / n))
    if s_ref == s:
        angle = (2*pi)/n
        print(angle)
        polygons +=1

