import pygame

pygame.init()
display = pygame.display.set_mode([512, 512])
font = pygame.font.Font(None, 24)

upper_limit = 20
iters = {}
max_so_far = 0
max_val = 0
scale = 23

for start in range(2, upper_limit + 1):
    display.fill("black")
    count = 0
    n = start
    while n != 1:
        count += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    iters[start] = count
    if len(iters.items()) >= 2:
        coords = [(x * scale, y * scale) for x, y in list(iters.items())]
        pygame.draw.lines(display, "white", False, coords)
        new_display = pygame.transform.flip(display, False, True)
        display.blit(new_display, (0, 0))
        pygame.display.flip()
    if count > max_so_far:
        max_so_far = count
        max_val = start
    string = f"The value with the max iterations so far is {max_val} with {max_so_far} iterations"
    msg = font.render(string, True, "white")
    display.blit(msg, (10, 10))
    pygame.display.flip()
    pygame.time.wait(500)
print(iters)
pygame.time.wait(3000)
