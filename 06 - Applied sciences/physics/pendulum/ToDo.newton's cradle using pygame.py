"""

https://www.youtube.com/watch?v=qN2UcshefrA

"""
import pygame
import numpy as np

# --- Simulation parameters ---
WIDTH, HEIGHT = 800, 400
BALL_RADIUS = 20
NUM_BALLS = 5
ROPE_LENGTH = 180
BALL_COLOR = (60, 60, 200)
BG_COLOR = (240, 240, 240)
FPS = 60
GRAVITY = 0.6

# --- Initial angles (displace the leftmost ball) ---
angles = np.zeros(NUM_BALLS)
angles[0] = np.radians(60)  # Displace the first ball

# --- Angular velocities ---
angular_vel = np.zeros(NUM_BALLS)

# --- Ball positions (horizontal spacing) ---
anchor_x = WIDTH // 2 - (NUM_BALLS // 2) * 2 * BALL_RADIUS
anchor_y = 80
anchors = [(anchor_x + i * 2 * BALL_RADIUS, anchor_y) for i in range(NUM_BALLS)]

# --- Initialize Pygame ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Newton's Cradle (5 Balls)")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Physics: update all balls as pendulums ---
    for i in range(NUM_BALLS):
        angular_acc = -GRAVITY / ROPE_LENGTH * np.sin(angles[i])
        angular_vel[i] += angular_acc
        angular_vel[i] *= 0.999  # Damping for stability
        angles[i] += angular_vel[i]

    # --- Improved collision logic: allow impulse to propagate through all balls ---
    # Detect all collisions and store them
    collisions = []
    positions = [anchors[i][0] + ROPE_LENGTH * np.sin(angles[i]) for i in range(NUM_BALLS)]
    for i in range(NUM_BALLS - 1):
        if abs(positions[i] - positions[i+1]) < 2 * BALL_RADIUS:
            # Balls are in contact
            collisions.append(i)

    # Propagate impulses through the chain
    for i in collisions:
        # Only transfer if balls are moving toward each other
        if angular_vel[i] > 0 and angular_vel[i+1] < 0:
            # Transfer the entire velocity to the last ball in the chain moving left to right
            j = i
            while j + 1 < NUM_BALLS and abs(positions[j] - positions[j+1]) < 2 * BALL_RADIUS and angular_vel[j+1] < 0:
                j += 1
            angular_vel[i], angular_vel[j] = 0, angular_vel[i]
            for k in range(i+1, j):
                angular_vel[k] = 0
        elif angular_vel[i] < 0 and angular_vel[i+1] > 0:
            # Transfer the entire velocity to the first ball in the chain moving right to left
            j = i + 1
            while j - 1 >= 0 and abs(positions[j] - positions[j-1]) < 2 * BALL_RADIUS and angular_vel[j-1] > 0:
                j -= 1
            angular_vel[i+1], angular_vel[j] = 0, angular_vel[i+1]
            for k in range(j+1, i+1):
                angular_vel[k] = 0

    # --- Drawing ---
    screen.fill(BG_COLOR)
    for i in range(NUM_BALLS):
        anchor = anchors[i]
        x = int(anchor[0] + ROPE_LENGTH * np.sin(angles[i]))
        y = int(anchor[1] + ROPE_LENGTH * np.cos(angles[i]))
        # Draw rope
        pygame.draw.line(screen, (80, 80, 80), anchor, (x, y), 3)
        # Draw ball
        pygame.draw.circle(screen, BALL_COLOR, (x, y), BALL_RADIUS)
        # Draw anchor
        pygame.draw.circle(screen, (0, 0, 0), anchor, 5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()