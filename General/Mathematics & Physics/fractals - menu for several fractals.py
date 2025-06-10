import pygame
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Initialize pygame for the menu system
pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Fractal Display Menu")
font = pygame.font.Font(None, 30)

# Define menu options
menu_options = [
    "Mandelbrot Fractal",
    "Koch Snowflake",
    "Julia Set",
    "Sierpiński Triangle",
    "Romanesco Broccoli (Approx.)",
    "Lightning & River Networks (Approx.)"
]

def mandelbrot():
    """Generates and displays the Mandelbrot Set."""
    width, height = 800, 800
    x_min, x_max, y_min, y_max = -2.0, 1.0, -1.5, 1.5
    max_iter = 256
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C, dtype=np.complex128)
    M = np.full(C.shape, True, dtype=bool)
    
    for _ in range(max_iter):
        Z[M] = Z[M]**2 + C[M]
        M[np.abs(Z) > 2] = False
    
    plt.imshow(M, cmap=cm.magma, extent=[x_min, x_max, y_min, y_max])
    plt.title("Mandelbrot Set")
    plt.show()

def display_menu():
    """Displays the menu and handles user input."""
    running = True
    while running:
        screen.fill((255, 255, 255))
        for idx, option in enumerate(menu_options):
            text = font.render(f"{idx+1}. {option}", True, (0, 0, 0))
            screen.blit(text, (50, 50 + idx * 40))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mandelbrot()
                elif event.key in [pygame.K_5, pygame.K_6]:
                    print("Approximate representation not implemented.")
                    
    pygame.quit()

display_menu()