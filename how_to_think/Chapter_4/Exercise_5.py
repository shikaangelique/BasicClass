import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
angelique = turtle.Turtle()
angelique.penup()
angelique.pendown()
angelique.pensize(3)
angelique.pencolor("blue")

length = 5
for i in range(100):
    angelique.forward(length)
    angelique.left(91)
    length += 5


window.exitonclick()

