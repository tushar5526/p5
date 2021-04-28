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



def setup():
    print("SETUP")
    p5.sketch.canvas.clear(skia.ColorWHITE)
    size(1000, 700)
    p5.renderer.render_rectangle(200, 300, 50, 50)
    print("frame count", frame_count)


def draw():
    if frame_count == 1:
        no_loop()
    p5.renderer.render_circle(20,20, 30)
    print("DRAW HEIHGT", height, width)
    # Enable this to render font
    render_font = True
    if render_font:
        p5.renderer.clear()
        myfont = p5.renderer.load_font('/home/tushar55/p5/p5/sketch/Skia2DRenderer/Quicksand-Ialic.otf')
        p5.renderer.set_font(myfont)
        p5.renderer.render_text("Left click to redraw", 100, 100)
        myfont = p5.renderer.load_font('/home/tushar55/p5/p5/sketch/Skia2DRenderer/LucidaSansRegular.ttf')
        p5.renderer.set_font(myfont)
        p5.renderer.set_font_size(40)
        p5.renderer.render_text("Right click to loop again", 50, 150)
        p5.renderer.set_font_size(10)
        p5.renderer.render_text(f"Frame Count {frame_count}", 5, 20)
        p5.renderer.set_font_size(60)
        p5.renderer.render_text("You can try resizing the window manually", 50, 200)
        p5.renderer.render_text("Try no loop at various places for testing", 50, 250)
    p5.renderer.render_circle(p5.sketch.mouseX, p5.sketch.mouseY, 30)

    # p5.renderer.render_rectangle(p5.sketch.mouseX, p5.sketch.mouseY, 100, 100)
    print("FRAME COUNT", frame_count)
    pass


if __name__ == '__main__':
    run(renderer='skia',  frame_rate=60)

