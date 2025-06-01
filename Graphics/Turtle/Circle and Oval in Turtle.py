# Circle and Oval in Turtle

import turtle

# Create a new window for drawing
window = turtle.Screen()
window.bgcolor("white")  # Set background color

# Create a turtle to draw a circle
circle_turtle = turtle.Turtle()
circle_turtle.penup()
circle_turtle.goto(-100, -50)  # Move to starting position
circle_turtle.shape("triangle")  # Set turtle shape
circle_turtle.color("blue")  # Set drawing color
circle_turtle.pendown()
circle_turtle.circle(100)  # Draw circle
circle_turtle.penup()

# Create a turtle to draw an oval
oval_turtle = turtle.Turtle()
oval_turtle.penup()
oval_turtle.goto(200, -50)  # Move to starting position
oval_turtle.pendown()

# Draw an oval using two arcs
for _ in range(2):
    oval_turtle.circle(120, 90)  # Small arc
    oval_turtle.circle(250, 90)  # Large arc

# Close window on click
window.exitonclick()