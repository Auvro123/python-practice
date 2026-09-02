import turtle
turtle.color('red','yellow')
turtle.begin_fill()
while True:    
    for i in range(1, 8):
        turtle.forward(200)
        turtle.left(60)
    if abs(turtle.position()) < 1:
        
        turtle.end_fill()
    turtle.done()

    turtle.exitonclick()