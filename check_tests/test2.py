from p5 import *

def setup():
    size(640, 360)
    no_stroke()
    no_loop()

def draw():
    draw_circle(width / 2, 280, 6)

def draw_circle(x, radius, level):
    tt = 126 * level / 4.0
    fill(tt)
    ellipse((x, height / 2), radius * 2, radius * 2)
    if level > 1:
        level = level - 1
        draw_circle(x - radius / 2, radius / 2, level)
        draw_circle(x + radius / 2, radius / 2, level)

if __name__ == '__main__':
    run()