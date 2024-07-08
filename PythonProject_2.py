from turtle import *

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        forward(size)
        right(90)

# Function to draw a dot at a given position
def draw_dot(x, y):
    penup()
    goto(x, y)
    pendown()
    dot(20)

# Function to draw dice face
def draw_dice_face(face, size):
    start_x = -size / 2
    start_y = size / 2

    # Draw dots according to the dice face number
    if face == 1:
        draw_dot(0, 0)
    elif face == 2:
        draw_dot(start_x + size / 4, start_y - size / 4)
        draw_dot(-start_x - size / 4, -start_y + size / 4)
    elif face == 3:
        draw_dot(start_x + size / 4, start_y - size / 4)
        draw_dot(0, 0)
        draw_dot(-start_x - size / 4, -start_y + size / 4)
    elif face == 4:
        draw_dot(start_x + size / 4, start_y - size / 4)
        draw_dot(-start_x - size / 4, start_y - size / 4)
        draw_dot(start_x + size / 4, -start_y + size / 4)
        draw_dot(-start_x - size / 4, -start_y + size / 4)
    elif face == 5:
        draw_dot(start_x + size / 4, start_y - size / 4)
        draw_dot(-start_x - size / 4, start_y - size / 4)
        draw_dot(0, 0)
        draw_dot(start_x + size / 4, -start_y + size / 4)
        draw_dot(-start_x - size / 4, -start_y + size / 4)
    elif face == 6:
        draw_dot(start_x + size / 4, start_y - size / 6)
        draw_dot(-start_x - size / 4, start_y - size / 6)
        draw_dot(start_x + size / 4, 0)
        draw_dot(-start_x - size / 4, 0)
        draw_dot(start_x + size / 4, -start_y + size / 6)
        draw_dot(-start_x - size / 4, -start_y + size / 6)

# Set up the turtle
speed(0)
hideturtle()

# Draw the square
penup()
goto(-50, 50)  # Starting position
pendown()
draw_square(100)

# Draw a dice face (change the number to 1-6 for different faces)
draw_dice_face(5, 100)

done()
