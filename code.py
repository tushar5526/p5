from p5 import *
import skia


def setup():
    print("SETUP")
    p5.sketch.canvas.clear(skia.ColorWHITE)
    size(800, 900)
    p5.renderer.render_rectangle(10, 10, 50, 50)
    # p5.sketch.looping = False

def draw():
    p5.renderer.render_circle(p5.sketch.mouseX, p5.sketch.mouseY, 10)
    p5.renderer.render_rectangle(p5.sketch.mouseX, p5.sketch.mouseY, 100, 100)
    print("frame count", frame_count)
    pass


if __name__ == '__main__':
    run(renderer='skia',  frame_rate=60)
