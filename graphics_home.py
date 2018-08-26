from graphics import *
points = []
cur_color = 'black'


def pt(x, y, window):
    print('making point with color', cur_color)
    p = Point(x,y)
    p.setFill(cur_color)
    p.draw(window)
    #points.append(p)

def col(new_color):
    global cur_color 
    cur_color = new_color
    #print(cur_color, new_color)

def drawing(w):
    pt(50,50,w)
    col('blue')
    pt(100,100,w)

def run_drawing():
    win = GraphWin("Graphics Window", 500, 500)
    drawing(win)
    """ for point in points:
        point.setFill(cur_color)
        point.draw(win) """

    win.getMouse()
    win.close()

run_drawing()

