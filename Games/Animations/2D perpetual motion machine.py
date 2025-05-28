"""
Ki:

Write a Python program. The program should display an animation of a 2D perpetual motion machine.

answer:
Creating an animation of a 2D perpetual motion machine is a fun challenge! While true perpetual motion 
machines defy the laws of physics, I can help you build an animated simulation that gives the illusion of endless motion.

"""

import pygame
import math

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 150, 250)
GRAY = (100, 100, 100)

# Parameters
radius = 50
angle = 0

running = True
while running:
    screen.fill(WHITE)

    # Calculate the position of the rotating arm
    x = WIDTH // 2 + radius * math.cos(math.radians(angle))
    y = HEIGHT // 2 + radius * math.sin(math.radians(angle))

    # Draw a static base
    pygame.draw.rect(screen, GRAY, (WIDTH//2 - 30, HEIGHT//2 + 20, 60, 10))

    # Draw a rotating arm
    pygame.draw.line(screen, BLUE, (WIDTH//2, HEIGHT//2), (x, y), 5)
    pygame.draw.circle(screen, BLUE, (int(x), int(y)), 10)

    # Update angle to create motion
    angle += 2
    if angle >= 360:
        angle = 0

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()