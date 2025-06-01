"""
Ki:

Write a Python program that will animate a bouncing ball.


answer:

This program initializes a pygame window and animates a red ball bouncing inside the screen. 
It updates the ball's position in a loop, checks for collisions with the screen edges, and reverses its direction accordingly.

"""
import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Balls")

# Ball properties
BALL_RADIUS = 20
COLORS = [(255, 0, 0), (0, 0, 255)]  # Red & Blue
balls = [
    {"x": random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS),
     "y": random.randint(BALL_RADIUS, HEIGHT - BALL_RADIUS),
     "dx": random.choice([-4, 4]),
     "dy": random.choice([-4, 4]),
     "color": COLORS[i]} for i in range(2)
]

def detect_collision(ball1, ball2):
    """Check if two balls collide"""
    distance = math.sqrt((ball1["x"] - ball2["x"])**2 + (ball1["y"] - ball2["y"])**2)
    return distance <= BALL_RADIUS * 2

running = True
while running:
    screen.fill((200, 200, 200))  # Light gray background
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for ball in balls:
        # Move ball
        ball["x"] += ball["dx"]
        ball["y"] += ball["dy"]

        # Bounce off walls
        if ball["x"] <= BALL_RADIUS or ball["x"] >= WIDTH - BALL_RADIUS:
            ball["dx"] *= -1
        if ball["y"] <= BALL_RADIUS or ball["y"] >= HEIGHT - BALL_RADIUS:
            ball["dy"] *= -1

        # Draw ball
        pygame.draw.circle(screen, ball["color"], (ball["x"], ball["y"]), BALL_RADIUS)

    # Check for collision between balls
    if detect_collision(balls[0], balls[1]):
        balls[0]["dx"], balls[1]["dx"] = -balls[0]["dx"], -balls[1]["dx"]
        balls[0]["dy"], balls[1]["dy"] = -balls[0]["dy"], -balls[1]["dy"]

    pygame.display.flip()
    pygame.time.delay(30)  # Control speed

pygame.quit()