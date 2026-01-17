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
COLORS = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0), (255, 0, 255)]  # Red, Blue, Green, Yellow, Magenta
balls = [
    {"x": random.randint(BALL_RADIUS, WIDTH - BALL_RADIUS),
     "y": random.randint(BALL_RADIUS, HEIGHT - BALL_RADIUS),
     "dx": random.choice([-4, -3, 3, 4]),
     "dy": random.choice([-4, -3, 3, 4]),
     "color": COLORS[i]} for i in range(5)
]

def detect_collision(ball1, ball2):
    """Check if two balls collide"""
    distance = math.sqrt((ball1["x"] - ball2["x"])**2 + (ball1["y"] - ball2["y"])**2)
    return distance <= BALL_RADIUS * 2

def handle_ball_collision(ball1, ball2):
    """Handle elastic collision between two balls with proper physics"""
    # Calculate distance between balls
    dx = ball2["x"] - ball1["x"]
    dy = ball2["y"] - ball1["y"]
    distance = math.sqrt(dx**2 + dy**2)
    
    # Prevent division by zero
    if distance == 0:
        distance = 0.01
    
    # Normalize the collision vector
    nx = dx / distance
    ny = dy / distance
    
    # Relative velocity
    dvx = ball2["dx"] - ball1["dx"]
    dvy = ball2["dy"] - ball1["dy"]
    
    # Relative velocity in collision normal direction
    dvn = dvx * nx + dvy * ny
    
    # Do not resolve if velocities are separating
    if dvn > 0:
        return
    
    # Calculate impulse scalar (assuming equal mass)
    impulse = -dvn
    
    # Apply impulse to both balls
    ball1["dx"] -= impulse * nx
    ball1["dy"] -= impulse * ny
    ball2["dx"] += impulse * nx
    ball2["dy"] += impulse * ny
    
    # Separate overlapping balls to prevent sticking
    overlap = BALL_RADIUS * 2 - distance
    if overlap > 0:
        separation = overlap / 2 + 0.5
        ball1["x"] -= separation * nx
        ball1["y"] -= separation * ny
        ball2["x"] += separation * nx
        ball2["y"] += separation * ny

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

        # Bounce off walls with position correction
        if ball["x"] <= BALL_RADIUS:
            ball["x"] = BALL_RADIUS
            ball["dx"] = abs(ball["dx"])
        elif ball["x"] >= WIDTH - BALL_RADIUS:
            ball["x"] = WIDTH - BALL_RADIUS
            ball["dx"] = -abs(ball["dx"])
            
        if ball["y"] <= BALL_RADIUS:
            ball["y"] = BALL_RADIUS
            ball["dy"] = abs(ball["dy"])
        elif ball["y"] >= HEIGHT - BALL_RADIUS:
            ball["y"] = HEIGHT - BALL_RADIUS
            ball["dy"] = -abs(ball["dy"])

        # Draw ball
        pygame.draw.circle(screen, ball["color"], (ball["x"], ball["y"]), BALL_RADIUS)

    # Check for collision between all pairs of balls
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            if detect_collision(balls[i], balls[j]):
                handle_ball_collision(balls[i], balls[j])

    pygame.display.flip()
    pygame.time.delay(30)  # Control speed

pygame.quit()