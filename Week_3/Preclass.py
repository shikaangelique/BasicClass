import turtle
window = turtle.Screen()

color = input("Would you like a lightgreen or red background?")
window.bgcolor(color)

window.title("Hello!")
tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)
tess.forward(50)
tess.left(120)

tess.forward(50)
window.mainloop()

number = 100


def drawmandy(number):
    for i in range(number):
        turtle.penup()
        turtle.forward(100)
        turtle.left(90)
        turtle.penup()
        turtle.forward(30)
        turtle.left(90)
        turtle.pendown()
        turtle.pencolor("#27ae60")
        turtle.forward(60)
        turtle.pencolor("#d35400")
        turtle.right(70)
        turtle.forward(70)
        turtle.right(40)
        turtle.forward(50)
        turtle.pencolor("#c0392b")
        turtle.left(90)
        turtle.pensize(5)
        turtle.forward(100)
        turtle.pencolor("#2980b9")
        turtle.left(90)
        turtle.forward(100)
        turtle.right(50)
        turtle.forward(70)
        turtle.pensize(10)
        turtle.left(60)
        turtle.pensize(6)
        turtle.forward(65)
        turtle.left(45)
        turtle.forward(120)


drawmandy(number)

