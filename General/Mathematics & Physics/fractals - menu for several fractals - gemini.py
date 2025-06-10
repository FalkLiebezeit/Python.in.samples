"""0
Copilot:
Write a Python program. The program should be able to display six fractals. 
A menu allows you to select which of the six fractals to display: 
Mandelbrot Fractal, Koch Snowflake, Julia Set, Sierpiński Triangle, 
Romanesco Broccoli, or Lightning and River Networks.

answer:
This program allows you to select and display six different fractals via a menu: 
Mandelbrot set, Koch snowflake, Julia set, Sierpiński triangle, 
a stylized 2D representation of Romanesco broccoli, and a lightning/river network fractal.

The libraries matplotlib, numpy, and turtle are used for rendering. 
Make sure they are installed (pip install matplotlib numpy


Code Explanations:

https://gemini.google.com/app/a37b2a0306496bcb

"""
import numpy as np
import matplotlib.pyplot as plt
import turtle
import math
import random

# --- 1. Mandelbrot Fractal ---
def mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter):
    """Generates the Mandelbrot fractal."""
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    C = np.array([complex(r, i) for r in x for i in y]).reshape(height, width)
    Z = np.zeros_like(C)
    N = np.zeros(C.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) < 2.0
        Z[mask] = Z[mask]**2 + C[mask]
        N[mask] = i

    N[np.abs(Z) >= 2.0] = max_iter # Set diverging points to max_iter
    return N

def display_mandelbrot():
    """Displays the Mandelbrot fractal."""
    print("Generating Mandelbrot fractal...")
    img = mandelbrot(width=800, height=600,
                     x_min=-2.0, x_max=1.0,
                     y_min=-1.5, y_max=1.5,
                     max_iter=100)
    plt.figure(figsize=(10, 7.5))
    plt.imshow(img, cmap='magma', extent=[-2.0, 1.0, -1.5, 1.5])
    plt.title("Mandelbrot Fractal")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.colorbar(label="Iterations until divergence")
    plt.show()

# --- 2. Koch Snowflake ---
def koch_segment(t, order, size):
    """Draws a segment of the Koch curve."""
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_segment(t, order - 1, size / 3)
            t.left(angle)

def display_koch_snowflake():
    """Displays the Koch snowflake."""
    print("Drawing Koch snowflake...")
    screen = turtle.Screen()
    screen.setup(width=800, height=700)
    screen.bgcolor("white")
    screen.tracer(0) # Turn off screen updates for faster drawing

    t = turtle.Turtle()
    t.speed(0) # Fastest speed
    t.hideturtle()
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    t.color("blue")

    order = 4 # Detail level of the snowflake
    size = 300  # Size of one side

    for _ in range(3):
        koch_segment(t, order, size)
        t.right(120)

    screen.update() # Update the screen to show the result
    turtle.done() # Keep the window open until closed

# --- 3. Julia Set ---
def julia_set(width, height, x_min, x_max, y_min, y_max, c_real, c_imag, max_iter):
    """Generates a Julia set."""
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    Z_real, Z_imag = np.meshgrid(x, y)
    Z = Z_real + 1j * Z_imag
    C = complex(c_real, c_imag)
    N = np.zeros(Z.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) < 2.0
        Z[mask] = Z[mask]**2 + C
        N[mask] = i

    N[np.abs(Z) >= 2.0] = max_iter
    return N

def display_julia_set():
    """Displays a Julia set."""
    print("Generating Julia set...")
    # Constants for c (can be varied for different Julia sets)
    c_real, c_imag = -0.7, 0.27015 # A classic value
    # c_real, c_imag = -0.8, 0.156
    # c_real, c_imag = 0.285, 0.01

    img = julia_set(width=800, height=600,
                    x_min=-1.5, x_max=1.5,
                    y_min=-1.0, y_max=1.0,
                    c_real=c_real, c_imag=c_imag,
                    max_iter=150)

    plt.figure(figsize=(10, 7.5))
    plt.imshow(img, cmap='inferno', extent=[-1.5, 1.5, -1.0, 1.0])
    plt.title(f"Julia Fractal (c = {c_real} + {c_imag}i)")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.colorbar(label="Iterations until divergence")
    plt.show()

# --- 4. Sierpiński Triangle ---
def draw_sierpinski_triangle(ax, points, level, colors):
    """Recursively draws the Sierpiński triangle."""
    if level == 0:
        triangle = plt.Polygon(points, color=colors[0])
        ax.add_patch(triangle)
    else:
        # Midpoints of the sides
        p1 = (points[0] + points[1]) / 2.0
        p2 = (points[1] + points[2]) / 2.0
        p3 = (points[2] + points[0]) / 2.0

        # Recursive calls for the three smaller triangles
        draw_sierpinski_triangle(ax, np.array([points[0], p1, p3]), level - 1, colors)
        draw_sierpinski_triangle(ax, np.array([p1, points[1], p2]), level - 1, colors)
        draw_sierpinski_triangle(ax, np.array(p3, p2, points[2]  ), level - 1, colors)

def display_sierpinski_triangle():
    """Displays the Sierpiński triangle."""
    print("Drawing Sierpiński triangle...")
    fig, ax = plt.subplots(figsize=(8, 7))

    # Corner points of the outer triangle
    points = np.array([[0.0, 0.0], [1.0, 0.0], [0.5, np.sqrt(0.75)]])
    level = 5 # Recursion depth

    ax.set_aspect('equal', adjustable='box')
    plt.axis('off') # Hide axes
    draw_sierpinski_triangle(ax, points, level, ["black", "white"]) # Color only for the lowest level
    plt.title(f"Sierpiński Triangle (Level {level})")
    plt.show()

# --- 5. Romanesco Broccoli (2D stylized representation) ---
def draw_romanesco_branch(ax, x, y, angle, length, level, max_level, base_color):
    """Recursively draws a branch of the Romanesco broccoli."""
    if level > max_level or length < 2:
        return

    x_end = x + length * np.cos(np.radians(angle))
    y_end = y + length * np.sin(np.radians(angle))

    # Color gets lighter with each level
    intensity = 0.3 + 0.7 * (1 - level / max_level)
    current_color = (base_color[0] * intensity, base_color[1] * intensity, base_color[2] * intensity)

    # Cone-like structure using circles
    num_circles = 5
    for i in range(num_circles):
        radius_factor = (1 - i / num_circles)
        circle_radius = length / (8 + level*2) * radius_factor
        if circle_radius < 0.5: circle_radius = 0.5 # Minimum radius
        
        center_x = x + (x_end - x) * (i / num_circles)
        center_y = y + (y_end - y) * (i / num_circles)
        
        circle = plt.Circle((center_x, center_y), circle_radius,
                            color=current_color, fill=True, alpha=0.8-level*0.1)
        ax.add_patch(circle)

    # Branching
    new_length = length * 0.65
    angle_offset_base = 35 + level * 5 # Larger angle for higher levels to suggest a spiral

    # Main spiral
    draw_romanesco_branch(ax, x_end, y_end, angle - angle_offset_base, new_length, level + 1, max_level, base_color)
    # Smaller side spiral
    draw_romanesco_branch(ax, x_end, y_end, angle + angle_offset_base * 0.8, new_length * 0.7, level + 1, max_level, base_color)


def display_romanesco_broccoli():
    """Displays a 2D stylized representation of Romanesco broccoli."""
    print("Drawing Romanesco broccoli (2D stylized)...")
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.set_facecolor('lightgray') # Background color
    plt.axis('off')

    max_level = 6
    base_color_rgb = (0.2, 0.8, 0.2) # Light green

    # Start from bottom to top
    initial_length = 100
    initial_angle = 90 # Upwards

    # Multiple starting points for a fuller base
    num_base_branches = 3
    for i in range(num_base_branches):
        angle_variation = (i - num_base_branches // 2) * 15
        draw_romanesco_branch(ax, 0 + i*10, 0, initial_angle + angle_variation,
                              initial_length * (1 - abs(i - num_base_branches // 2) * 0.1),
                              0, max_level, base_color_rgb)

    ax.set_xlim(-150, 150)
    ax.set_ylim(0, 250)
    plt.title("Romanesco Broccoli (2D stylized representation)")
    plt.show()

# --- 6. Lightning and River Networks (Fractal Tree) ---
def draw_lightning_branch(ax, x1, y1, angle, length, depth, max_depth, color="cyan", initial_lw=4):
    """Recursively draws a lightning or river branch."""
    if depth > max_depth or length < 1:
        return

    x2 = x1 + length * np.cos(np.radians(angle))
    y2 = y1 + length * np.sin(np.radians(angle))
    
    lw = initial_lw * ((max_depth - depth + 1) / max_depth)**1.5 # Thickness decreases
    if lw < 0.5: lw = 0.5

    ax.plot([x1, x2], [y1, y2], color=color, linewidth=lw, solid_capstyle='round')

    new_length = length * (0.7 + random.uniform(-0.1, 0.1)) # Some variation in length
    
    # Two main branches
    angle1 = angle + random.uniform(15, 40) # Random angle for branch 1
    angle2 = angle - random.uniform(15, 40) # Random angle for branch 2

    draw_lightning_branch(ax, x2, y2, angle1, new_length, depth + 1, max_depth, color, initial_lw)
    draw_lightning_branch(ax, x2, y2, angle2, new_length, depth + 1, max_depth, color, initial_lw)

    # Optional smaller, shorter branch
    if random.random() < 0.3: # 30% chance for a third, smaller branch
        angle3 = angle + random.uniform(-10, 10)
        draw_lightning_branch(ax, x2, y2, angle3, new_length * 0.5, depth + 1, max_depth, color, initial_lw)


def display_lightning_network():
    """Displays a lightning or river network fractal."""
    print("Drawing lightning/river network...")
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.set_facecolor('black') # Dark background for lightning
    plt.axis('off')

    max_depth = 8
    initial_length = 60
    initial_angle_main = 90 # Main direction (upwards)

    # Starting point in the bottom center
    start_x, start_y = 0, -200

    # Multiple main lightning bolts/rivers from one origin point
    num_main_branches = 3
    for i in range(num_main_branches):
        angle_variation = random.uniform(-10, 10) + (i - num_main_branches//2)*5
        length_variation = initial_length * random.uniform(0.9, 1.1)
        draw_lightning_branch(ax, start_x, start_y, initial_angle_main + angle_variation,
                              length_variation, 0, max_depth, color="cyan", initial_lw=3)

    ax.set_xlim(-250, 250)
    ax.set_ylim(-200, 200)
    plt.title("Lightning / River Network Fractal")
    plt.show()


# --- Main Menu ---
def main_menu():
    """Displays the main menu and processes user input."""
    while True:
        print("\n--- Fractal Generator ---")
        print("Select a fractal to display:")
        print("1. Mandelbrot Fractal")
        print("2. Koch Snowflake")
        print("3. Julia Set")
        print("4. Sierpiński Triangle")
        print("5. Romanesco Broccoli (2D stylized)")
        print("6. Lightning / River Network")
        print("0. Exit")

        choice = input("Your choice (0-6): ")

        if choice == '1':
            display_mandelbrot()
        elif choice == '2':
            # Turtle requires special handling for repeated execution
            try:
                turtle.Screen().clear() # Tries to clear the previous turtle screen
                turtle.Screen().reset()
            except turtle.Terminator: # If the window was already closed
                pass
            except Exception as e:
                print(f"Error resetting Turtle: {e}")
            display_koch_snowflake()
        elif choice == '3':
            display_julia_set()
        elif choice == '4':
            display_sierpinski_triangle()
        elif choice == '5':
            display_romanesco_broccoli()
        elif choice == '6':
            display_lightning_network()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid input. Please choose a number between 0 and 6.")

if __name__ == "__main__":
    main_menu()