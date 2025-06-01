"""
Ki:

Write a Python program. 
The program should display an animation of a 2D perpetual motion machine.
You can modify the event handling so that pressing the "ESC" key (pygame.K_ESCAPE) will terminate the program.


answer:

This Python program creates a simple **rotating arm simulation** using Pygame. Here's a breakdown of its functionality:

### **1. Initialization**  
- **Pygame is initialized** with `pygame.init()`.  
- A **600x400 pixel screen** is created using `pygame.display.set_mode()`.  
- `clock = pygame.time.Clock()` ensures controlled frame rate updates.

### **2. Colors & Parameters**  
- `WHITE`, `BLUE`, and `GRAY` define colors for the background, rotating arm, and base.  
- `radius = 50` defines the distance of the moving point from the center.  
- `angle = 0` is the **starting angle** for rotation.

### **3. Main Loop**  
The loop continuously updates the screen and ensures animation:

#### **A. Calculate the Position of the Rotating Arm**  
Using trigonometry, the arm’s endpoint (`x, y`) is determined:  
- `x = WIDTH // 2 + radius * cos(angle)`: Moves the endpoint **horizontally**.  
- `y = HEIGHT // 2 + radius * sin(angle)`: Moves the endpoint **vertically**.

#### **B. Draw Elements**  
- A **static base** (gray rectangle) represents the pivot point.  
- A **blue line** connects the center with the rotating point.  
- A **blue circle** marks the endpoint of the rotating arm.

#### **C. Update the Angle**  
The angle is incremented by `2` degrees per frame, creating a smooth **circular motion**.  
Once `angle >= 360`, it resets to `0` to continue rotating.

#### **D. Event Handling**  
If the user **closes the window**, the program exits gracefully.

### **4. Display Updates**  
- `pygame.display.flip()` refreshes the screen.  
- `clock.tick(30)` controls the animation speed to **30 FPS**.

### **End Result:**  
This program generates a **continuous rotating arm animation** with a **smooth circular motion**, ideal for visualizing basic physics concepts like rotation!

Let me know if you want modifications! 🚀


"""
import pygame
import math

# Initialize pygame
pygame.init()

# Enlarged screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 150, 250)
GRAY = (100, 100, 100)

# Updated parameters
radius = 120  # Increased pendulum length
angle = 0

running = True
while running:
    screen.fill(WHITE)

    # Calculate position of the pendulum arm
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

    # Handle events (Exit if "ESC" key is pressed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()