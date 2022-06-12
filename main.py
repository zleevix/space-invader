from cProfile import run
import pygame

# Initalize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))
# Change title
pygame.display.set_caption("Space Invaders")
# Change icon pygame
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

running = True

while running:
    # catch event QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print("KEYDOWN")
    # RGB 
    screen.fill((255,0,0))

    # Update while running
    pygame.display.update()