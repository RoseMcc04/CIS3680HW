"""
File: circle.py
Project 7.1

Draws a circle.

1. The inputs are the coordinates of the center point and the radius.

"""

import math
from turtle import Turtle

def drawCircle(t, x, y, radius):
    """Draws a circle with the given center point and radius."""

    # Initializing the drawing
    t.penup()
    t.goto(x, y - radius)
    t.pendown()

    # Incremented distance formula
    distance = 2.0 * math.pi * radius / 120.0

    # Loop that draws the circle
    for _ in range(120):
        t.forward(distance)
        t.left(3)
    

def main():
    x = 50
    y = 65
    radius = 100
    drawCircle(Turtle(), x, y, radius)

if __name__ == "__main__":
    main()
