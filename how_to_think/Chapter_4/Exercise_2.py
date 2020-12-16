import turtle, math, random

def draw_square(shika, length):
    for i in range(4):
        shika.forward(length)
        shika.left(90)
    shika.penup()

window = turtle.Screen()
window.bgcolor("lightgreen")
angelique = turtle.Turtle()
angelique.pensize(5)
angelique.pencolor("hotpink")
angelique.penup()

length = 20

for i in range(5):
    angelique.backward(10)
    angelique.right(90)
    angelique.forward(10)
    angelique.left(90)
    angelique.pendown()
    draw_square(angelique, length)
    length += 20





window.exitonclick()