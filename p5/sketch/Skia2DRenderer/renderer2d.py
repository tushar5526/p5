import contextlib, glfw, skia
from OpenGL import GL

from p5 import p5


class SkiaRenderer():
    def __init__(self):
        self.canvas = None
        self.paint = None
        self.style = None
        self.path = None

    def initialize_renderer(self, canvas, paint, path):
        self.canvas = canvas
        self.paint = paint
        self.path = path
        self.canvas.clear(skia.ColorWHITE)

    def render_rectangle(self, x, y, w, h):
        # print("called rectangel")
        self.path.moveTo(x, y)
        self.path.lineTo(x + w, y)
        self.path.lineTo(x + w, y + h)
        self.path.lineTo(x, y + h)
        self.render()

    def render_circle(self, x, y, radius):
        self.path.addCircle(x, y, radius)
        self.render()

    def render_text(self, text, x, y):
        font = skia.Font()
        self.canvas.drawSimpleText(text, x, y, font, self.paint)
        print("Called render text")
        # self.canvas.drawText(text, x, y, self.paint)

    def clear(self):
        self.canvas.clear(skia.ColorWHITE)

    def render(self, rewind=True):
        """
        Draw the path on current canvas using paint
        """
        print(self.path.countVerbs())
        # print(self.canvas)
        print("RENDER NOW")
        self.paint.setColor(skia.ColorRED)
        self.paint.setStyle(skia.Paint.kFill_Style)
        self.canvas.drawPath(self.path, self.paint)
        self.paint.setColor(skia.ColorCYAN)
        self.paint.setStyle(skia.Paint.kStroke_Style)
        self.canvas.drawPath(self.path, self.paint)
        if rewind and p5.sketch.resized:
            print("REWINDED")
            self.path.rewind()
