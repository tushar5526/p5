from p5 import *
import skia


def setup():
    print("SETUP")
    p5.sketch.canvas.clear(skia.ColorWHITE)
    size(500, 500)
    p5.renderer.render_rectangle(200, 300, 50, 50)
    print("frame count", frame_count)


def draw():
    p5.renderer.clear()
    p5.renderer.render_circle(20,20, 30)
    p5.renderer.render_text("Left click to redraw", 100, 100)
    p5.renderer.render_text("Right click to loop again", 100, 150)
    p5.renderer.render_text("You can try resizing the window manually", 100, 200)
    p5.renderer.render_text("Try no loop at various places for testing", 100, 250)
    p5.renderer.render_circle(p5.sketch.mouseX, p5.sketch.mouseY, 30)

    # p5.renderer.render_circle(200,100, 30)
    # p5.renderer.render_rectangle(100, 10, 50, 50)

    # p5.renderer.render_rectangle(p5.sketch.mouseX, p5.sketch.mouseY, 100, 100)
    print("frame count", frame_count)
    pass


if __name__ == '__main__':
    run(renderer='skia',  frame_rate=60)

