import math
import pygame
import random

pygame.init()

WIDTH = 500
HEIGHT = 500
RED = [255, 0, 0]
BLUE = [0, 0, 255]
BLACK = [0, 0, 0]
LIGHT_BLUE = [173, 216, 230]
SALMON = [255, 140, 105]
BLACK = [0, 0, 0]

screen = pygame.display.set_mode([HEIGHT, WIDTH])

# Choose which player will win
red_button_box = pygame.Rect(0, HEIGHT / 4, HEIGHT / 2, WIDTH / 2)
blue_button_box = pygame.Rect(0, 0, HEIGHT / 2, WIDTH / 2)
blue_button_box.topleft = red_button_box.topright
red_button = pygame.draw.rect(screen, RED, red_button_box)
blue_button = pygame.draw.rect(screen, BLUE, blue_button_box)
pygame.display.flip()

guess = 0
print(
    "Please select the player who you think will win by clicking on the player color."
)
while guess == 0:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            if red_button_box.collidepoint(mouse_click_pos):
                guess = 1
            if blue_button_box.collidepoint(mouse_click_pos):
                guess = 2

# Set up board
screen.fill(LIGHT_BLUE)
pygame.draw.circle(screen, SALMON, (HEIGHT / 2, WIDTH / 2), HEIGHT / 2)
pygame.draw.line(screen, BLACK, (0, HEIGHT / 2), (WIDTH, HEIGHT / 2))
pygame.draw.line(screen, BLACK, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
pygame.display.flip()

player1_score = 0
player2_score = 0

# main game loop
for i in range(10):
    print(f"#ROUND{i + 1}")
    for j in range(2):
        x_pos = random.randrange(0, WIDTH + 1)
        y_pos = random.randrange(0, HEIGHT + 1)
        distance_from_center = math.hypot(x_pos - WIDTH / 2, y_pos - HEIGHT / 2)
        is_in_circle = distance_from_center <= WIDTH / 2
        if is_in_circle:
            if j == 0:
                pygame.draw.circle(screen, RED, (x_pos, y_pos), 4)
                player1_score += 1
                print(f"player red throws...hit")
            else:
                pygame.draw.circle(screen, BLUE, (x_pos, y_pos), 4)
                player2_score += 1
                print(f"player blue throws...hit")
        else:
            pygame.draw.circle(screen, BLACK, (x_pos, y_pos), 4)
            if j == 0:
                print(f"player red throws...miss")
            else:
                print(f"player red throws...miss")
        pygame.display.flip()
        pygame.time.wait(500)

# print winners
print(f"Player Red scored {player1_score}")
print(f"Player Blue scored {player2_score}")
print()
if player1_score > player2_score:
    print("Player Red Won!")
    if guess == 1:
        print("Your guess was correct!")
    else:
        print("Your guess is wrong!")
elif player1_score < player2_score:
    print("Player Blue Won!")
    if guess == 2:
        print("Your guess was correct!")
    else:
        print("Your guess is wrong!")
else:
    print("This was a tie")
    print("Your guess is wrong!")

pygame.time.wait(3000)
pygame.quit()
