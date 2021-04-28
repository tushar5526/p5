from p5 import *

def draw():
    circle(30, 30, 30)
    print(frame_count)
    if frame_count == 100:
        exit()

if __name__ == '__main__':
    run()