import builtins
from p5.core import p5

import contextlib, glfw, skia
from OpenGL import GL
from time import time
from time import time

#
# class SkiaSketch():
#     def __init__(self, setup_method, draw_method,
#                  handlers=None, frame_rate=60):
#         # different environment variables
#         self.frame_count = 0
#         self.delta_time = 0
#         self._size = (360, 360)
#         self.looping = None
#
#         # Different variables which will be used by
#         # sketch and renderer to perform different functions
#         # default canvas, path, and paint variables
#         self.canvas = None
#         self.path = None
#         self.paint = None
#
#     # create a glfw window
#     # create path and paint objects
#     # assign callbacks, environment variables, renderer variables
#     # start the main loop
#     def start(self):
#         pass
#
#     # resize, screenshot, etc.
#     # callbacks handler similar to vispy Sketch()
#     def other_functions(self):
#         pass


class SkiaSketch():
    def __init__(self, setup_method, draw_method, frame_rate=60):
        self.frame_count = 0
        self._size = (600, 400)
        self.setup_method = setup_method
        self.draw_method = draw_method
        self.surface = None
        self.context = None
        self.window = None
        self.canvas = None
        self.mouseX = 0
        self.mouseY = 0
        self.main_loop_state = True
        self.looping = True
        self.paint = skia.Paint()
        self.paint.setAntiAlias(True)
        self.path = skia.Path()
        self.frame_rate = frame_rate

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, val):
        self._size = val
        self.resize()

    def clean_up(self):
        glfw.terminate()
        self.context.abandonContext()

    def glfw_window(self):
        if not glfw.init():
            raise RuntimeError('glfw.init() failed')
        glfw.window_hint(glfw.STENCIL_BITS, 8)
        window = glfw.create_window(*self._size, 'Testing', None, None)
        glfw.make_context_current(window)
        return window

    def skia_surface(self, window, size):
        print("surface created")
        self.context = skia.GrContext.MakeGL()
        backend_render_target = skia.GrBackendRenderTarget(
            *size,
            0,  # sampleCnt
            0,  # stencilBits
            skia.GrGLFramebufferInfo(0, GL.GL_RGBA8))
        surface = skia.Surface.MakeFromBackendRenderTarget(
            self.context, backend_render_target, skia.kBottomLeft_GrSurfaceOrigin,
            skia.kRGBA_8888_ColorType, skia.ColorSpace.MakeSRGB())
        assert surface is not None
        return surface

    def assign_callbacks(self):
        glfw.set_cursor_pos_callback(self.window, self.mouse_callback_handler)
        glfw.set_framebuffer_size_callback(self.window, self.frame_buffer_resize_callback_handler)

    def create_surface(self, size=None):
        print("create surface")
        if not size:
            size = self._size
        self.surface = self.skia_surface(self.window, size)
        self.canvas = self.surface.getCanvas()
        p5.renderer.initialize_renderer(self.canvas, self.paint, self.path)

    def poll_events(self):
        glfw.poll_events()
        if (glfw.get_key(self.window, glfw.KEY_ESCAPE) == glfw.PRESS or glfw.window_should_close(self.window)):
            glfw.set_window_should_close(self.window, 1)
            self.main_loop_state = False

    def main_loop(self):
        last_render_call_time = time()
        while (self.main_loop_state):
            if self.looping and (time() - last_render_call_time) > 1/self.frame_rate:
                builtins.frame_count += 1
                with self.surface as self.canvas:
                    self.draw_method()
                    p5.renderer.render()
                self.surface.flushAndSubmit()
                glfw.swap_buffers(self.window)
                last_render_call_time = time()
            self.poll_events()

    def start(self):
        self.window = self.glfw_window()
        self.create_surface()
        self.assign_callbacks()
        p5.renderer.initialize_renderer(self.canvas, self.paint, self.path)
        self.setup_method()
        self.poll_events()
        print("before buffers ", glfw.get_window_size(self.window), self._size)
        p5.renderer.render(rewind=False)
        self.surface.flushAndSubmit()
        glfw.swap_buffers(self.window)
        print("BEFORE MAIN")
        self.main_loop()
        self.clean_up()

    def mouse_callback_handler(self, window, xpos, ypos):
        # print(xpos, ypos)
        self.mouseX = xpos
        self.mouseY = ypos
        return

    def frame_buffer_resize_callback_handler(self, window, width, height):
        print("FRAME BUFFER CALLBACK NOW ")
        print("frame buffer size callback ", glfw.get_window_size(self.window))
        GL.glViewport(0, 0, width, height)
        self.create_surface(size=(width, height))
        with self.surface as self.canvas:
            p5.renderer.render()
        self.surface.flushAndSubmit()
        glfw.swap_buffers(self.window)

    def resize(self):
        self.create_surface()
        glfw.set_window_size(self.window, *self.size)

        print(glfw.get_framebuffer_size(self.window), self._size, glfw.get_window_size(self.window))
