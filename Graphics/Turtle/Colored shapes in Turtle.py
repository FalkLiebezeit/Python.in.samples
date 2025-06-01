# Colored shapes in Turtle

import turtle

# Set up the turtle screen
window = turtle.Screen()
window.bgcolor("white")  # Set background color to white

# Create a turtle for drawing
turtle1 = turtle.Turtle()
turtle1.speed(5)  # Set drawing speed (5 = normal)

# Set the fill color and begin filling
turtle1.fillcolor("yellow")
turtle1.begin_fill()

# Draw a filled circle with a radius of 150 pixels
turtle1.circle(150)

# Complete the fill process
turtle1.end_fill()

# Keep the window open until the user closes it
turtle.done()
