import turtle

def draw_square(shika, length):
    for i in range(4):
        shika.forward(length)
        shika.left(90)

window = turtle.Screen()
window.bgcolor("lightgreen")
angelique = turtle.Turtle()
angelique.penup()
angelique.goto(-200, 0)
angelique.pendown()
angelique.pensize(5)
angelique.pencolor("hotpink")

for i in range(5):
    draw_square(angelique,50)
    angelique.penup()
    angelique.forward(100)
    angelique.pendown()




window.exitonclick()

