import skia, warnings
from contextlib import contextmanager
from p5.sketch.Skia2DRenderer.renderer2d import StyleClass
from p5 import *

# A list which stores all the active PGraphics objects
active_pGraphics = []

# Cache the current default values of the sketch
# Replace the the default values with PGraphics object's values
# Render
# Reset the values
@contextmanager
def draw_graphics(graphics):
    # cache the default values
    global _image_mode
    default_canvas = p5.renderer.canvas
    default_paint = p5.renderer.paint
    default_path = p5.renderer.path
    default_image_mode = _image_mode
    default_font = p5.renderer.font
    default_typeface = p5.renderer.typeface
    default_style = p5.renderer.style
    # Replace with new values
    p5.renderer.canvas = graphics.canvas
    p5.renderer.paint = graphics.paint
    p5.renderer.path = graphics.path
    p5.renderer.font = graphics.font
    p5.renderer.typeface = graphics.typeface
    p5.renderer.style = graphics.style
    _image_mode = graphics._image_mode
    # draw to the graphics' canvas using path and
    # paint
    yield
    # Reset them back to old values
    p5.renderer.canvas = default_canvas
    p5.renderer.paint = default_paint
    p5.renderer.path = default_path
    p5.renderer.font = default_font
    p5.renderer.typeface = default_typeface
    p5.renderer.style = default_style
    _image_mode = default_image_mode

class PGraphics():
    def __init__(self, width, height, *args):
        array = np.zeros((height, width, 4), dtype=np.uint8)
        self.canvas = skia.Canvas(array)
        self.path = skia.Path()
        self.paint = skia.Paint()
        self.font = skia.Font()
        self.typeface = skia.Typeface.MakeDefault()
        self.font.setTypeface(self.font)
        self._image_mode = 'CORNERS'
        self._blend_mode = None
        self.style = None
        self.style = StyleClass()
        # .
        # .
        # .
        active_pGraphics.append(self)

    # wrapper around p5, will be called like
    # Pgraphics_Object.rect(0, 0, 100, 100)
    def rect(self, *args):
        with draw_graphics(self):
            image(*args)

    def image(self, *args):
        with draw_graphics(self):
            image(*args)