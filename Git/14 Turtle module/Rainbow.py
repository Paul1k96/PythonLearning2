from turtle import *

hideturtle(), Screen().setup(600, 600), speed(0)
Screen().colormode(255)  # for Python3
rainbow_colors = [(255, 0, 0), (255, 120, 0), (255, 255, 0), (128, 255, 0), (0, 255, 0), (0, 255, 80),
                  (0, 255, 255), (0, 128, 255), (0, 0, 255), (128, 0, 255), (255, 0, 255), (255, 0, 128)]

size, mv = 300, -300
for i in rainbow_colors:
    penup(), goto(0, mv), pendown()
    begin_fill(), fillcolor(i)
    circle(size)
    end_fill()
    mv += 25  # move up
    size -= 25

done()
