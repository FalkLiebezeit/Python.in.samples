"""
Ki:

Write a Python program that will animate a bouncing ball.


answer:

This program initializes a pygame window and animates a red ball bouncing inside the screen. It updates the ball's position in a loop, checks for collisions with the screen edges, and reverses its direction accordingly.

"""

import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
ball_radius = 20
x, y = WIDTH // 2, HEIGHT // 2
dx, dy = 4, 4  # Change in x and y

# Clock for controlling frame rate
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    # Move the ball
    x += dx
    y += dy

    # Bounce off walls
    if x - ball_radius <= 0 or x + ball_radius >= WIDTH:
        dx = -dx
    if y - ball_radius <= 0 or y + ball_radius >= HEIGHT:
        dy = -dy

    # Draw the ball
    pygame.draw.circle(screen, RED, (x, y), ball_radius)

    # Refresh the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()