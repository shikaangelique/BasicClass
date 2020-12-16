import turtle

def draw_polygon(poly, sides, length):
    for n in range(sides):
        poly.forward(length)
        poly.left(360/sides)
    poly.penup


window = turtle.Screen()
window.bgcolor("lightgreen")
angelique = turtle.Turtle()
angelique.penup()
angelique.pendown()
angelique.pensize(3)
angelique.pencolor("blue")

length= 100
for i in range(36):
    draw_polygon(angelique, 4, length)
    angelique.left(10)





window.exitonclick()