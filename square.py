import turtle


def slated_square():
    turtle.setheading(45)
    turtle.forward(75)
    turtle.setheading(315)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(75)


def half_slated_square():
    turtle.setheading(45)
    turtle.forward(75)
    turtle.setheading(315)
    turtle.forward(75)


def square():
    turtle.setheading(90)
    turtle.forward(75)
    turtle.setheading(180)
    turtle.forward(75)
    turtle.setheading(270)
    turtle.forward(75)
    turtle.setheading(0)
    turtle.forward(75)


def reversed_square():
    turtle.forward(75)
    turtle.setheading(270)
    turtle.forward(75)
    turtle.setheading(180)
    turtle.forward(75)
    turtle.setheading(90)
    turtle.forward(75)


def cube():
    turtle.reset()
    turtle.hideturtle()
    square()
    reversed_square()
    turtle.left(45)
    turtle.forward(105)
    turtle.goto(0, 0)
    turtle.setheading(315)
    turtle.forward(105)
    turtle.penup()
    turtle.goto(0, -75)
    turtle.pendown()
    turtle.setheading(135)
    turtle.forward(105)
    turtle.penup()
    turtle.goto(0, 75)
    turtle.setheading(315)
    turtle.pendown()
    turtle.forward(105)


def sets():
    turtle.circle(25)
    turtle.right(45)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.circle(25)


def tangled():
    sets()
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(0)
    turtle.forward(65)
    turtle.pendown()
    sets()
    turtle.penup()
    turtle.goto(72, 0)
    turtle.setheading(0)
    turtle.forward(59)
    turtle.pendown()
    sets()


def axis():
    turtle.reset()
    turtle.hideturtle()
    turtle.setheading(90)
    turtle.forward(100)
    turtle.write('North')

    turtle.goto(0, 0)
    turtle.setheading(0)
    turtle.forward(100)
    turtle.write('East')

    turtle.goto(0, 0)
    turtle.setheading(180)
    turtle.forward(100)
    turtle.write('West')

    turtle.goto(0, 0)
    turtle.setheading(270)
    turtle.forward(100)
    turtle.write('South')
    turtle.penup()
    turtle.goto(-20, 0)
    turtle.pendown()
    turtle.circle(20)
