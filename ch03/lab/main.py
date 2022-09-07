import turtle #1. import modules
import random
import pygame
import math

# #Part A
# window = turtle.Screen() # 2.  Create a screen
# window.bgcolor('lightblue')

# michelangelo = turtle.Turtle() # 3.  Create two turtles
# leonardo = turtle.Turtle()
# michelangelo.color('orange')
# leonardo.color('blue')
# michelangelo.shape('turtle')
# leonardo.shape('turtle')

# michelangelo.up() # 4. Pick up the pen so we don’t get lines
# leonardo.up()
# michelangelo.goto(-100,20)
# leonardo.goto(-100,-20)

# ## 5. Your PART A code goes here
# michelangelo.forward(random.randrange(1, 101))
# leonardo.forward(random.randrange(1, 101))
# michelangelo.goto(-100, 20)
# leonardo.goto(-100, -20)
# for i in range(10):
#     michelangelo.forward(random.randrange(1, 11))
#     leonardo.forward(random.randrange(1, 11))
# michelangelo.goto(-100, 20)
# leonardo.goto(-100, -20)


# window.exitonclick()


# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode([500, 500])
window.fill((255, 255, 255))
coords = []
num_sides = 5
side_length = 100
offset = 20
for i in range(num_sides):
    theta = (2.0 * math.pi * num_sides) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    coords.append((x, y))
pygame.draw.polygon(window, "white", coords)
pygame.time.wait(2000)