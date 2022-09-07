import turtle

window = turtle.Screen()
bob = turtle.Turtle(shape="turtle")
bob.pencolor("purple")
for i in range(4):
    bob.forward(50)
    bob.left(90)
bob.up()
bob.pencolor("red")
bob.forward(90)
bob.down()
for i in range(4):
    bob.forward(50)
    bob.left(90)

window.exitonclick()
