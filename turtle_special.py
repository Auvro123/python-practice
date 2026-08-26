import turtle
turtle.color('red','yellow')
turtle.begin_fill()
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.position()) < 1:
        
        turtle.end_fill()
    turtle.done()

    turtle.exitonclick()