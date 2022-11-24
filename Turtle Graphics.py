import turtle

import square

turtle.speed(20)
turtle.hideturtle()
square.slated_square()
square.half_slated_square()
square.slated_square()

turtle.clear()

turtle.reset()
turtle.hideturtle()
square.half_slated_square()
turtle.setheading(180)
turtle.forward(107)

turtle.setheading(65)
turtle.forward(126)
turtle.setheading(295.5)
turtle.forward(128)

turtle.clear()

square.cube()

turtle.clear()
turtle.reset()

square.tangled()

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

turtle.done()
