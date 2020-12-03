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



