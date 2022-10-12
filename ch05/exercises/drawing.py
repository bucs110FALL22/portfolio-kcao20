import turtle


def drawEqShape(t, num_sides, side_length):
    theta = 360 / num_sides
    for i in range(num_sides):
        t.forward(side_length)
        t.left(theta)


window = turtle.Screen()


num_sides = int(input("Enter the number of sides to draw: "))
side_length = int(input("Enter the side length of each side: "))

bob = turtle.Turtle()
bob.shape("turtle")
bob.color("green")

drawEqShape(bob, num_sides, side_length)

window.exitonclick()
