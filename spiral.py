import turtle
import random

turtle.color("green")
turtle.colormode(255)
turtle.shape("turtle")
turtle.speed(0)
for i in range(200):
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    turtle.forward(120)
    turtle.left(60)
    turtle.forward(i*2)
    turtle.right(10)
    turtle.pencolor(r,g,b)

turtle.exitonclick()