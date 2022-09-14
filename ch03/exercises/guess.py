import random

randNum = random.randint(1, 10)
for i in range(3):
    guess = int(input("Enter a guess from 1 to 10: "))
    if guess == randNum:
        print("correct!")
        break
    elif guess > randNum:
        print("Too High")
    else:
        print("Too Low")
