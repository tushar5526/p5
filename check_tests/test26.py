from p5 import *

xvals = None
yvals = None
bvals = None
arrayindex = 0

def setup():
        size(640, 360)

        global xvals, yvals, bvals
        xvals = [0]*width
        yvals = [0]*width
        bvals = [0]*width

def draw():
        background(102);

        global xvals, yvals, bvals
        for i in range(1, width):
                xvals[i-1] = xvals[i]
                yvals[i-1] = yvals[i]
                bvals[i-1] = bvals[i]

        xvals[width - 1] = mouse_x
        yvals[width - 1] = mouse_y

        if mouse_is_pressed:
                bvals[width-1] = 0;
        else:
                bvals[width-1] = 255;


        fill(255)
        no_stroke()
        rect((0, height/3), width, height/3+1)

        for i in range(1, width):
                stroke(255)
                point(i, remap(xvals[i], [0, width], [0, height/3 - 1]))
                stroke(0)
                point(i, height/3 + yvals[i]/3)
                stroke(255)
                line([i, 2*height/3 + bvals[i]/3], [i, (2*height/3 + bvals[i - 1]/3)])

if __name__ == '__main__':
        run()