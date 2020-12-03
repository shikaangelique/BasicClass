import turtle


def draw_polygon(drawing_turtle: turtle.Turtle, sides=4, size=25):
    for side in range(sides):
        drawing_turtle.forward(size)
        drawing_turtle.left(360 / sides)

screen = turtle.Screen()

#  nick = turtle.Turtle()
#  draw_polygon(nick)

selly = turtle.Turtle()

for no_sides in range(3, 12):
    draw_polygon(selly, no_sides, 10 * no_sides)

#  mayday = turtle.Turtle
#  draw_polygon(mayday, 7, 150)


screen.exitonclick()
