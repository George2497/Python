# Let's draw some cool drawings with the package turtle

# Import turtle
import turtle


# Let's get a nice set-up in turtle
turtle.bgcolor("black")  # Background colour
turtle.pensize(2)  # Pen size
turtle.color("red")  # Pen colour
turtle.speed(0)  # The speed of how quick turtle draws

# Draw a square
# turtle.forward(50)  # Moves forward
# turtle.left(170)  # Moves left 90 degrees
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(90)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.done()  # Allows turtle to stay on the screen

# Nice little project in turtle - creates a nice graphic
# for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
#     turtle.color(colours)
#     turtle.circle(150)
#     turtle.left(60)
# turtle.done()

# Let's make it cooler
for i in range(12):
    for colours in ["red", "orange", "yellow", "green", "blue", "purple"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(5)
turtle.done()
