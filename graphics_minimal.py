from graphics import *
import numpy as np

cur_color = 'black'
background = 'white'
width = 400
height = 500
win = None


def pt(x, y):
    p = Point(x,y)
    p.setFill(cur_color)
    p.draw(win)

def rect(x, y, w, h):
    for i in range(h):
        for j in range(w):
            pt(x+j, y+i)

def line(x0, y0, x1, y1):
    # All lines go left to right
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    dx = x1 - x0
    dy = y1 - y0
    derror = abs(dy / float(dx))
    print(x0, y0, x1, y1, derror)
    error = 0
    y = y0
    for x in range(x0, x1):
        pt(x,y)
        error = error + derror
        if error >= 0.5:
            y = y + np.sign(dy) 
            error = error + 1

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
