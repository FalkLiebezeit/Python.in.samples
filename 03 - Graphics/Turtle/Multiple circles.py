# multiple circles in turtle
# https://docs.python.org/3/library/turtle.html

import turtle

# Create a new window for drawing
window = turtle.Screen()
window.bgcolor("gray")  # Set background color

# Create a turtle to draw a circle
circle_turtle = turtle.Turtle()

circle_turtle.penup()
circle_turtle.goto(0, -250)  # Move to starting position
#circle_turtle.shape("triangle")  # Set turtle shape
circle_turtle.color("blue")  # Set drawing color
circle_turtle.pensize(1)  # Set pen size
circle_turtle.pendown()

"""
#for i in range(0,5):
for _ in range(1):
    circle_turtle.circle(100)  # Draw circle
    circle_turtle.circle(120) 
    circle_turtle.circle(250)

"""


for i in range(1,15):
#for _ in range(1):
    circle_turtle.circle(i * 15)  # Draw circle
   



circle_turtle.penup()

"""
# Create a turtle to draw an oval
oval_turtle = turtle.Turtle()
oval_turtle.penup()
oval_turtle.goto(200, -50)  # Move to starting position
oval_turtle.pendown()


# Draw an oval using two arcs
for _ in range(2):
    oval_turtle.circle(120, 90)  # Small arc
    oval_turtle.circle(250, 90)  # Large arc
"""


# Close window on click
window.exitonclick()