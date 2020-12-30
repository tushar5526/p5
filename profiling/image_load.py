from p5 import *

def setup():
    size(200, 200)

def draw():
    background(200)

    # Two vectors, one for the mouse location and one of the center
    # of the window
    mouse = Vector(mouse_x, mouse_y)
    center = Vector(width / 2, height / 2)

    # Vector subtraction!
    mouse = mouse - center
    # The magnitude (i.e., the length) of a vector can be accessed by
    # the mag() function. Here it is used as the width of a rectangle
    # drawn at the top of the window.
    m = mouse.magnitude
    print(m)
    fill(0)
    rect((0, 0), m, 10)

    # Draw a line to represent the vector
    translate(center.x, center.y)
    line((0, 0), (mouse.x, mouse.y))

if __name__ == '__main__':
    run()