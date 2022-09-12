import turtle

numSides = int(input("Enter the number of sides: "))
sideLength = int(input("Enter the length of each side: "))
window = turtle.Screen()
t1 = turtle.Turtle()
t1.pencolor("lavender")
for i in range(numSides):
    t1.forward(sideLength)
    t1.left(360 / numSides)

window.exitonclick()
