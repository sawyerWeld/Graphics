from graphics import *
import numpy as np

cur_color = 'black'
background = 'white'
width = 400
height = 500
win = None


def pt(coords):
    x,y = coords
    p = Point(x,y)
    p.setFill(cur_color)
    p.draw(win)


def rect(x, y, w, h):
    for i in range(h):
        for j in range(w):
            pt(x+j, y+i)


def line(start, end):
    x0,y0 = start
    x1,y1 = end
    dx = x1 - x0
    dy = y1 - y0

    # Handle vertical lines
    if dx == 0:
        if y0 > y1:
            y1,y0 = y0,y1
        for i in range(y0,y1):
            pt((x0,i))
        return

    # Lines go left to right
    if x0 > x1:
        print('swap')
        x0,x1 = x1,x0
        y0,y1 = y1,y0

    # If slope > 1, we rotate
    rotated = False
    if (abs(dy) > abs(dx)):
        rotated = True
        x0,y0 = y0,x0
        x1,y1 = y1,x1
    
    dx = x1 - x0
    dy = y1 - y0

    err = int(dx / 2.0)
    y_inc = 1 if y0 < y1 else -1

    y = y0
    for x in range(x0, x1 + 1):
        point = (y, x) if rotated else (x, y)
        pt(point)
        # print(point[0], point[1])
        err -= abs(dy)
        if err < 0:
            y += y_inc
            err += dx


def col(new_color):
    global cur_color 
    cur_color = new_color


def set_background(color):
    global background
    background = color


def set_dimensions(w, h):
    global width, height
    width = w
    height = h


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

