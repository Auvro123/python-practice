import turtle
import random

turtle.colormode(255)
turtle.speed(0)
turtle.begin_fill()
turtle.bgcolor(0,0,0)

for _ in range(1,200):
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    turtle.pencolor(r,g,b)
    turtle.forward(200)
    turtle.left(160)
    turtle.right(_)
    turtle.forward(10)

turtle.end_fill()

turtle.exitonclick()