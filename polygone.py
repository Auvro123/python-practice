import turtle

turtle.color("green")

turtle.shape("turtle")
turtle.speed(5)
def draw_polygon(side_length, sides):
    for n in range(sides):
        turtle.forward(side_length)
        turtle.left(360/sides)

draw_polygon(10,96)
turtle.exitonclick()