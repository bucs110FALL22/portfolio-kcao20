import math
import random
import turtle


def main():
    canvSize = int(input("Enter how big you want the square canvas to be in pixels: "))

    bgColor, hullColor, mastColor, sailColor, flagColor = randomColors()

    # set up canvas
    window = turtle.Screen()
    window.setup(canvSize, canvSize)
    window.colormode(255)
    window.bgcolor(bgColor)

    # create turtle
    bob = turtle.Turtle()
    bob.speed(0)
    bob.hideturtle()
    bob.pu()
    # draw the hull of the boat
    bob.goto(-canvSize / 3, -canvSize / 6)
    bob.color(hullColor)
    bob.begin_fill()
    bob.setheading(-60)
    radius = (
        canvSize / 3 / math.sin(60 / 180 * math.pi)
    )  # make the hull of the boat 2/3 of screen canvSize
    bob.circle(radius, 120)
    bob.end_fill()

    # draw middle mast
    bob.goto(0, -canvSize / 6)
    drawmast(bob, canvSize, 1, 10, mastColor)
    drawFlag(bob, canvSize, 1, 0, flagColor)
    bob.goto(0, canvSize / 6)
    drawSail(bob, canvSize, (2 / 3), 0, sailColor)
    bob.goto(0, 0)
    drawSail(bob, canvSize, 1, 0, sailColor)

    # draw left mast
    bob.goto(-canvSize / 5, -canvSize / 6)
    drawmast(bob, canvSize, 0.8, 15, mastColor)
    drawFlag(bob, canvSize, 1, 0, flagColor)
    bob.goto(-canvSize / 4, canvSize / 6)
    drawSail(bob, canvSize, 1 / 2, 0, sailColor)
    bob.goto(-canvSize / 5, 0)
    drawSail(bob, canvSize, 2 / 3, 0, sailColor)

    # draw right mast
    bob.goto(canvSize / 5, -canvSize / 6)
    drawmast(bob, canvSize, 0.7, -10, mastColor)
    bob.goto(canvSize / 4, 0)
    drawSail(bob, canvSize, 1, -20, sailColor)

    window.exitonclick()


def randomColors():
    """
    Chooses random colors for each part of the ship
    """
    bgColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    hullColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    mastColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    sailColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    flagColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return bgColor, hullColor, mastColor, sailColor, flagColor


def drawmast(t: turtle, canvSize, length=1, tilt=0, color="saddle brown"):
    """
    Draws a mast
    args: t [turtle] the turtle that will be doing the drawing
          canvSize [int] the size of the canvas
          length [float] how lost the mast is
          tilt [float] the angle the mast is tilted
          color [str] the color of the sail
    """
    t.color(color)
    t.pensize(canvSize ** (1 / 3))
    t.setheading(90 + tilt)
    t.pd()
    t.forward(canvSize * length / 2)
    t.pu()


def drawSail(t: turtle, canvSize, size=1, tilt=-10, color="white"):
    """
    Draws a sail utilizing circle function to draw arcs
    args: t [turtle] the turtle that will be doing the drawing
          canvSize [int] the size of the canvas
          size [float] the scaling of the sail
          tilt [int] the angle the sail is tilted
          color [str] the color of the sail
    """
    t.setheading(-45)
    t.forward(size * canvSize * 7 / 50)
    t.setheading(150 + tilt)
    t.color(color)
    t.begin_fill()
    t.circle(size * -canvSize * 7 / 50, 120)
    t.left(180)
    t.forward(size * canvSize * 2 / 7)
    t.left(20)
    t.circle(size * canvSize / 10, 120)
    t.left(70)
    t.circle(size * -canvSize * 7 / 50, 90)
    t.end_fill()


def drawFlag(t: turtle, canvSize, size=1, tilt=0, color="red"):
    """
    Draws a flag
    args: t [turtle] the turtle that will be doing the drawing
          canvSize [int] the size of the canvas
          size [float] the scaling of the size of the flag
          tilt [int] the angle the flag is tilted
          color [str] the color of the flag
    """
    t.color(color)
    t.begin_fill()
    t.setheading(210 + tilt)
    t.forward(size * canvSize / 8)
    t.right(210 + tilt)
    t.forward(size * canvSize / 8)
    t.end_fill()


main()
