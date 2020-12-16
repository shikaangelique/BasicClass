import turtle

def draw_star(star):
    for i in range(5):
        star.forward(100)
        star.right(144)
    star.penup()

window = turtle.Screen()
window.bgcolor("lightgreen")
angelique = turtle.Turtle()
angelique.pencolor("hotpink")

for i in range(5):
    draw_star(angelique)
    angelique.penup()
    angelique.forward(350)
    angelique.right(144)
    angelique.pendown()

window.exitonclick()