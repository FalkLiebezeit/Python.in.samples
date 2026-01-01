import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball with Gravity")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
ball_radius = 20
ball_x, ball_y = WIDTH // 2, 100  # Start higher up
ball_speed_x, ball_speed_y = 4, 0  # Start with no vertical speed
GRAVITY = 0.5  # Gravity acceleration
BOUNCE_DAMPING = 0.8  # Energy loss on bounce (0-1, where 1 = no loss)
MIN_BOUNCE_SPEED = 1.0  # Minimum vertical speed to consider ball as bouncing

def reset_ball():
    """Reset ball to starting position"""
    return WIDTH // 2, 100, 4, 0

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

    # Apply gravity to vertical speed
    ball_speed_y += GRAVITY
    
    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce on side walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_speed_x *= -1
        # Correct position to prevent ball getting stuck
        if ball_x - ball_radius < 0:
            ball_x = ball_radius
        else:
            ball_x = WIDTH - ball_radius
    
    # Bounce on top
    if ball_y - ball_radius < 0:
        ball_speed_y *= -1
        ball_y = ball_radius
    
    # Bounce on plate with damping
    if ball_y + ball_radius > plate_y:
        ball_y = plate_y - ball_radius
        
        # Check if ball has enough energy to bounce
        if abs(ball_speed_y) < MIN_BOUNCE_SPEED:
            # Ball has stopped bouncing - reset it
            ball_x, ball_y, ball_speed_x, ball_speed_y = reset_ball()
        else:
            ball_speed_y *= -BOUNCE_DAMPING  # Reverse and dampen

    # Draw plate and ball
    pygame.draw.rect(screen, RED, (0, plate_y, WIDTH, plate_height))
    pygame.draw.circle(screen, RED, (int(ball_x), int(ball_y)), ball_radius)

    pygame.display.update()
    clock.tick(60)

pygame.quit()