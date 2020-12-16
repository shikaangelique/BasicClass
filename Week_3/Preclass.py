import turtle
window = turtle.Screen()

color = input("Would you like a lightgreen or red background?")
window.bgcolor(color)

window.title("Hello!")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")
tess.pensize(3)
tess.forward(50)
tess.left(120)

tess.forward(50)

for ahwehwe in [color, "yellow", "red","purple", ]:
    tess.color(ahwehwe)
    tess.forward(50)
    tess.left(90)

window.exitonclick()


