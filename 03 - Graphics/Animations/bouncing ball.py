import pygame

# --- Initialize pygame and set up the window ---
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Animation")

# --- Define colors ---
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# --- Ball properties ---
ball_radius = 20
x, y = WIDTH // 2, HEIGHT // 2      # Start in the center
dx, dy = 4, 4                       # Velocity in x and y

# --- Set up the clock for consistent frame rate ---
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    # --- Handle events (e.g., window close) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Update ball position ---
    x += dx
    y += dy

    # --- Bounce off the window edges ---
    if x - ball_radius <= 0 or x + ball_radius >= WIDTH:
        dx = -dx
        x += dx  # Prevent sticking to the wall
    if y - ball_radius <= 0 or y + ball_radius >= HEIGHT:
        dy = -dy
        y += dy  # Prevent sticking to the wall

    # --- Drawing section ---
    screen.fill(WHITE)  # Clear the screen
    pygame.draw.circle(screen, RED, (x, y), ball_radius)  # Draw the ball

    pygame.display.flip()  # Update the display

    clock.tick(FPS)  # Maintain consistent frame rate

pygame.quit()