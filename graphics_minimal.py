from graphics import *
import numpy as np

cur_color = 'black'
col_r = 100000000
col_g = 100000
col_b = 100
background = 'white'
width = 400
height = 500
stroke_w = 1
win = None
# The testing buffer is an expiremental testing feature
# Everytime a pixel is painted, the testing buffer is updated as well
# This makes testing the program much simpler
testing_mode = True
testing_buffer = None

def pt(coords):
    x,y = coords
    if (x >= width or y >= height):
        return
    p = Point(x,y)
    p.setFill(cur_color)
    p.draw(win)
    if testing_mode:
        global testing_buffer
        testing_buffer[x][y] = col_r + col_g + col_b


def stroke(w):
    global stroke_w
    stroke_w = w


def rect(x, y, w, h):
    for i in range(h):
        for j in range(w):
            pt((x+j, y+i))


def line(start, end):
    x0,y0 = start
    x1,y1 = end
    dx = x1 - x0
    dy = y1 - y0
    pts = []
  
    # If slope > 1, we rotate
    rotated = False
    if (abs(dy) > abs(dx)):
        rotated = True
        x0,y0 = y0,x0
        x1,y1 = y1,x1
    
    # Lines go left to right
    # If they dont, swap the points
    if x0 > x1:
        x0,x1 = x1,x0
        y0,y1 = y1,y0
    dx = x1 - x0
    dy = y1 - y0
    err = int(dx / 2.0)
    y_inc = 1 if y0 < y1 else -1
    

    y = y0
    for x in range(x0, x1 + 1):
        for i in range(stroke_w):
            point = (y+i, x) if rotated else (x, y+i)
            pt(point)
            pts.append(point)
        err -= abs(dy)
        if err < 0:
            y += y_inc
            err += dx

    return pts


def circle(center, r):
    arc = []
    x_c, y_c = center
    p = 1.25 - r
    x, y = (0, r)
    while x < y:
        if p < 0:
            p += 2*x + 1
        else:
            y -= 1
            p += 2*x + 1 - 2*y
        arc.append((x,y))
        x += 1
    for p in arc:
        x,y = p
        for x_sign in [-1, 1]:
            for y_sign in [-1,1]:
                x_hat = x_sign * x + x_c
                y_hat = y_sign * y + y_c
                pt((x_hat,y_hat))
                pt((y_hat,x_hat))

def col(new_color):
    global cur_color, col_r, col_g, col_b
    if isinstance(new_color, tuple):
        r,g,b = new_color
        col_r = r * 1000000
        col_g = g * 1000
        col_b = b
        cur_color = color_rgb(r,g,b)
    else:
        cur_color = new_color


def save_file(filename):
    save(filename)


def set_background(color):
    global background
    background = color


def set_dimensions(w, h):
    global width, height, testing_buffer
    width = w
    height = h
    testing_buffer = np.zeros((width,height), dtype = np.int)


def run_drawing(setup_function, draw_function):
    global win
    setup_function()
    win = GraphWin("Graphics Window", width, height, autoflush=False)
    win.setBackground(background)
    draw_function()
    # I'd like to have the window hang until the user presses enter
    # I'd use python's input() method but the terminal doesn't
    # stay focused when the graphics window opens
    win.getMouse()
    win.close()

