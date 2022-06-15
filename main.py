from cProfile import run
import pygame

# Initalize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

# Flag check game running: like threading python
running = True
while running:
    # catch event QUIT
    for event in pygame.event.get():
        # without the window open/close immediately
        if event.type == pygame.QUIT: # Catch when user click X to close pygame window
            running = False
        elif event.type == pygame.KEYDOWN:
            print("KEYDOWN")

    # Update while running
    pygame.display.update()