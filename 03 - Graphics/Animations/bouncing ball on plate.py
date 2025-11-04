import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Without Gravity")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
ball_radius = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 4, -4

# Plate properties
plate_height = 20
plate_y = HEIGHT - plate_height

# Clock for frame rate control
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce on walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_speed_x *= -1
    if ball_y - ball_radius < 0 or ball_y + ball_radius > plate_y:
        ball_speed_y *= -1

    # Draw plate and ball
    pygame.draw.rect(screen, RED, (0, plate_y, WIDTH, plate_height))
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

    pygame.display.update()
    clock.tick(60)

pygame.quit()