import turtle


def draw_polygon(poly, sides, length):
    for n in range(sides):
        poly.forward(length)
        poly.left(360 / sides)
    poly.penup()

def draw_equitriangle(triangle, size):
    draw_polygon(triangle, 3, size)

window = turtle.Screen()
window.bgcolor("lightgreen")
angelique = turtle.Turtle()
angelique.penup()
angelique.pendown()
angelique.pensize(3)
angelique.pencolor("hotpink")

draw_equitriangle(angelique, 200)

window.exitonclick()
