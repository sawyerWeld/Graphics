import graphics_minimal as gm
import numpy as np
import shapes
from time import sleep

width = 800
height = 800


def setup():
    gm.set_dimensions(width, height)
    gm.set_background('black')

def draw():
    # test_grids(mode = 1)
    gm.col((150,0,150))
    # print(gm.testing_buffer)
    # starburst()
    # rect(200,200,50,50)
    # gm.line((100,100),(110,75))
    # gm.circle((400,400),100)
    # gm.line((0,0), (400, 100))
    mySquare = shapes.Square(50,70,100)
    
    # mySquare.draw()
    shapes.draw_all()
    sleep(1000)
    shapes.translation(100,0,0)
    shapes.draw_all()
    # polygon_fill((50,50), (500,50), (500,500), (300,100))
    # octagon()

def polygon_fill(*args):
    verts = list(args)
    print(verts)
    y_min = 10000
    y_max = 0
    x_min = 10000
    x_max = 0
    for v in verts:
        x, y = v
        if x < x_min:
            x_min = x
        elif x > x_max:
            x_max = x
        if y < y_min:
            y_min = y
        elif y > y_max:
            y_max = y

    pts = []
    for i in range(len(verts)-1):
        pts += gm.line(verts[i], verts[i+1])
    pts += gm.line(verts[0], verts[-1])

    print(x_min, x_max, y_min, y_max)
    for y in range(y_min, y_max+1):
        passed = 0
        for x in range(x_min, x_max+1):
            if (x,y) in verts:
                break
            if (x,y) in pts:
                passed += 1
            elif passed % 2 == 1:
                gm.pt((x,y))
    
def starburst():
    x,y = (400,400)
    theta = np.pi
    r = 300
    n = 100    
    for _ in range(0,n):
        x0 = int(x + r * np.sin(theta))
        y0 = int(y + r * np.cos(theta))
        gm.line((x,y),(x0,y0))
        theta += 2*np.pi/n


def octagon():
    pts = []
    x,y = (400,400)
    theta = np.pi
    r = 300
    n = 100    
    for _ in range(0,n):
        x0 = int(x + r * np.sin(theta))
        y0 = int(y + r * np.cos(theta))
        pts.append((x0,y0))
        theta += 2*np.pi/n
        # theta += 50
    polygon_fill(*pts)
    

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
            gm.pt((x+j, y+i))

gm.run_drawing(setup_function = setup, draw_function = draw)

