"""
Copilot:

Write a Python program. 
The program should display two periodic functions in the range -2 pi to 2 pi. 
A menu allows you to select which function to display: sine curve or cosine curve.

"""
import numpy as np
import matplotlib.pyplot as plt

def plot_function(choice):
    x = np.linspace(-2 * np.pi, 2 * np.pi, 200)
    if choice == "sine":
        y = np.sin(x)
        title = "Sine Curve"
    elif choice == "cosine":
        y = np.cos(x)
        title = "Cosine Curve"
    else:
        print("Invalid choice! Please select 'sine' or 'cosine'.")
        return

    plt.plot(x, y)
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.show()

def main():
    while True:
        print("\nSelect a function to display:")
        print("1. Sine Curve")
        print("2. Cosine Curve")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            plot_function("sine")
        elif choice == "2":
            plot_function("cosine")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
