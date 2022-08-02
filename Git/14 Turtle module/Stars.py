from turtle import *
from random import randrange

tracer(100), hideturtle(), penup()
colormode(255)  # for Python3

for i in range(100):
    fillcolor(randrange(256), randrange(256), randrange(256))   # random color
    goto(randrange(-200-i, 200+i), randrange(-200-i, 200+i))    # random coord
    setheading(randrange(360))                                  # random angle
    size = randrange(10, 30)                                    # random size

    begin_fill()
    for _ in range(5):
        lt(144)
        fd(size)
    end_fill()

done()  # stop-command in IDE(turtle module)
