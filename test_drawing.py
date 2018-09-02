import graphics_minimal as gm
import numpy as np
width = 800
height = 800


def setup():
    gm.set_dimensions(width, height)
    back = gm.color_rgb(100, 0 , 255)
    gm.set_background('black')

def draw():
    # test_grids(mode = 1)
    gm.col((150,0,150))
    # print(gm.testing_buffer)
    starburst()

def starburst():
    x,y = (400,400)
    theta = np.pi
    r = 300
    n = 100
    for i in range(0,n):
        x0 = int(x + r * np.sin(theta))
        y0 = int(y + r * np.cos(theta))
        gm.line((x,y),(x0,y0))
        theta += 2*np.pi/n

def test_grids(mode = 0, inc = 50):
    h = 0
    while h < height:
        gm.line((0,h),(width,h))
        h += inc
    w = 0
    while w < width:
        gm.line((w,0),(w,height))
        w += inc

def rect(x, y, w, h):
    for i in range(h):
        for j in range(w):
            gm.pt(x+j, y+i)

gm.run_drawing(setup_function = setup, draw_function = draw)
