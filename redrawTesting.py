from p5 import *
import skia

"""
Features supported
    NoLoop()
    Loop()
    Resizing of the window
    Mouse click detection 
    Font rendering
    Basic Shape rendering
"""


x = 0

def setup():
    print("SETUP")
    p5.sketch.canvas.clear(skia.ColorWHITE)
    no_loop()

def draw():
    p5.sketch.canvas.clear(skia.ColorWHITE)

    print(frame_count)
    global x
    print(sketch_width, sketch_height)
    p5.renderer.render_circle(x % sketch_height, x % sketch_width, 30)
    x += 10



if __name__ == '__main__':
    run(renderer='skia',  frame_rate=60)

