from graphics import *
cur_color = 'black'
background = 'white'
width = 400
height = 500
win = None


def pt(x, y):
    print('making point with color', cur_color)
    p = Point(x,y)
    p.setFill(cur_color)
    p.draw(win)

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
    win = GraphWin("Graphics Window", width, height)
    win.setBackground(background)
    draw_function()
    win.getMouse() # Waits until mouse has been pressed in window
    win.close()
