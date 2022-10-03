import turtle
import random

window = turtle.Screen()
window.bgcolor("lavender")

bob = turtle.Turtle()

while (
    -turtle.window_height() / 2 <= bob.ycor() <= turtle.window_height() / 2
    and -turtle.window_width() / 2 <= bob.xcor() <= turtle.window_width() / 2
):
    if random.random() >= 0.5:
        bob.left(90)
    else:
        bob.right(90)
    bob.forward(50)

window.exitonclick()
