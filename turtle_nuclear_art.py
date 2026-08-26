import turtle

turtle.color("green")

turtle.shape("turtle")
turtle.speed(0)
for i in range(500):
    turtle.right(i)
    turtle.forward(10+i)

turtle.exitonclick()