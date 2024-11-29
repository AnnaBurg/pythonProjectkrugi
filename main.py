import pygame
from random import randint

pygame.init()
width, height = 500, 500

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Жёлтые окружности')

screen.fill((0, 0, 0))

for i in range(10):
    ew, eh = randint(1, 100), randint(1, 100)
    ex, ey = randint(1, 400), randint(1, 400)
    r, b, g = randint(0, 255), randint(0, 255), randint(0, 255)
    pygame.draw.ellipse(screen, (r, b, g), (ex, ey, ew, eh))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

