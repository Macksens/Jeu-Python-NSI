import pygame
import sys
from genese import genese

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Project_V1_aquatic_world")

# Set up the clock for a decent framerate
clock = pygame.time.Clock() 

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here

    # Drawing code goes here
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
sys.exit()