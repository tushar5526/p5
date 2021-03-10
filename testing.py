from p5 import *
import skia
import numpy as np
import matplotlib.pyplot as plt

width, height = 200, 200
array = np.zeros((height, width, 4), dtype=np.uint8)

canvas = skia.Canvas(array)
paint = skia.Paint(Color=skia.Color(255,0,0,20))
paint.setAntiAlias(True)
canvas.drawCircle(100, 100, 40, paint)
paint.setColor(skia.Color(0,255,0,100))
canvas.drawCircle(150, 100, 40, paint)
from p5 import  *
push_style()
plt.imshow(array)
plt.show()
#
# def setup():
#     print("SETUP")
#     p5.sketch.canvas.clear(skia.ColorWHITE)
#     size(1000, 700)
#     p5.renderer.render_rectangle(200, 300, 50, 50)
#     print("frame count", frame_count)
#
#
# def draw():
#     if frame_count == 1:
#         no_loop()
#     p5.renderer.render_circle(20,20, 30)
#     p5.renderer.render_circle(p5.sketch.mouseX, p5.sketch.mouseY, 30)
#     print("frame count", frame_count)
#
#
# if __name__ == '__main__':
#     run(renderer='skia',  frame_rate=60)
