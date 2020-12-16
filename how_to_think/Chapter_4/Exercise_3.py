import turtle


def draw_polygon(poly, sides, length):
    for n in range(sides):
        poly.forward(length)
        poly.left(360 / sides)
    poly.penup()


window = turtle.Screen()
window.bgcolor("lightgreen")
angelique = turtle.Turtle()
angelique.penup()
angelique.pendown()
angelique.pensize(3)
angelique.pencolor("hotpink")

draw_polygon(angelique, 8, 50)

window.exitonclick()
