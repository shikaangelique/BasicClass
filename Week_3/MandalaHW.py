import turtle


paper = turtle.Screen()
paper.bgcolor("white")
paper.title("Mandy the Mandala")
mandy = turtle.Turtle()
mandy.speed(0)
mandy.pensize(2)

radius_one = 140

mandy.up()
mandy.goto(-150, -200)
mandy.begin_fill()
mandy.color("grey")
mandy.pendown()
mandy.forward(300)
mandy.left(90)
mandy.forward(400)
mandy.left(90)
mandy.forward(300)
mandy.left(90)
mandy.forward(400)
mandy.left(90)
mandy.end_fill()

mandy.up()
mandy.begin_fill()
mandy.color("pink")
mandy.fillcolor('pink')
mandy.goto(0, -radius_one)
mandy.down()
mandy.circle(radius_one)
mandy.up()
mandy.pensize(5)
mandy.end_fill()

mandy.goto(0, 0)
mandy.down()
for j in range(10):
    mandy.begin_fill()
    mandy.right(360 / 10)
    mandy.color('grey')
    for i in range(4):
        mandy.forward(radius_one - 45)
        mandy.left(90)
    mandy.end_fill()

mandy.up()
mandy.color("pink")
mandy.begin_fill()
mandy.goto(0, -90)
mandy.down()
mandy.circle(90)
mandy.end_fill()

mandy.up()
mandy.goto(0, 0)
mandy.down
for j in range(6):
    mandy.begin_fill()
    mandy.left(360 / 6)
    mandy.color('grey')
    mandy.fillcolor("grey")
    for i in range(6):
        mandy.forward(43)
        mandy.left(360 / 6)
    mandy.end_fill()

mandy.penup()
mandy.goto(0, -54)
mandy.color("pink")
mandy.pendown()
mandy.circle(54)

mandy.penup()
mandy.goto(-43, 16)
mandy.pendown()
mandy.pencolor('pink')
for _ in range(5):
    mandy.forward(86)
    mandy.right(144)

mandy.penup()
mandy.goto(-100, 160)
mandy.pendown()
mandy.write('IF CAPTAIN AMERICA', font=("Arial", 20, "normal"))

mandy.penup()
mandy.goto(-120, -180)
mandy.pendown()
mandy.write('WAS A 12 YEAR OLD GIRL', font=("Arial", 20, "bold", "italic"))



mandy.hideturtle()
paper.exitonclick()
