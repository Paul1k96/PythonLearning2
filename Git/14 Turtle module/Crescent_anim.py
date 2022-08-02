from turtle import *

hideturtle(), Screen().bgcolor('DarkBlue'), penup()
dot(300, 'orange')

blue = Turtle('circle')
blue.hideturtle()
cnt = 310
blue.shapesize(15), blue.color('DarkBlue'), blue.penup(), blue.speed('fastest')
while True:
    for i in range(310):
        blue.goto(cnt-(i*2), 0)
        blue.showturtle()
    blue.hideturtle()
