import skia, warnings
from contextlib import contextmanager
from p5.sketch.Vispy2DRenderer import renderer2d
from p5.core import p5
from p5.core.image import _image_mode
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

    # Replace with new values
    p5.renderer.canvas = graphics.canvas
    p5.renderer.paint = graphics.paint
    p5.renderer.path = graphics.path
    _image_mode = graphics._image_mode

    # draw to the graphics' canvas using path and
    # paint
    yield

    # Reset them back to old values
    p5.renderer.canvas = default_canvas
    p5.renderer.paint = default_paint
    p5.renderer.path = default_path
    _image_mode = default_image_mode

class PGraphics():
    def __init__(self, width, height, *args):
        self.canvas = skia.Canvas(width, height)
        self.path = skia.Path()
        self.paint = skia.Paint()
        self._image_mode = 'CORNERS'
        self._blend_mode = None
        self.style_stack = []
        # .
        # .
        # .
        active_pGraphics.append(self)

    # wrapper around p5

    def image(self, *args):
        with draw_graphics(self):
            image(*args)