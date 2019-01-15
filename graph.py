from graphics import *
import graphics_objects as g
import itertools
import copy
import text

# Redoing graphics because it became a software engineering mess
win = None # have to have this at global level to use zelle graphics
width = 400
height = 400
real_space =  [['black' for j in range(width)] for i in range(height)]
cur_color = 'green'
zoom_level = 1
camera_position = (200,200)
screen_objects = g.group() # the objects we want displayed

def pt(coords):
    x,y = coords
    real_space[x][y] = cur_color

def put_txt(coords, str, color = 'white'):
    global cur_color
    cur_color = color
    li = text.text_points(str)
    x_coord, y_coord = coords
    pt_list = [(x+x_coord, y+y_coord) for x,y in li]
    for point in pt_list:
        pt(point)

def draw_function():
    # pt((10,10))
    # ln = g.line((10,10), (10, 100))
    sqr = g.square((50,250),100)
    crl = g.cirle((200,200),50)
    ply = g.polygon([(10,110),(55,60),(100,110),(100,200),(55,150),(10,200)], color='red', fill='white')
    sqr2 = copy.deepcopy(sqr)
    crl2 = copy.deepcopy(crl)
    sqr2.scale(.5)
    crl2.scale(.75)
    sqr2.color = 'red'
    crl2.color = 'green'
    put_txt((100,100), 'abcdefghijklmnopqrstuvwxyz()/.')
    put_txt((100,110), 'This line should be just below that one',color='pink')
    # make this into a method in the polgon object 
    # screen_objects.add(sqr)
    screen_objects.add_multiple([ply, sqr, sqr2, crl, crl2])
    
    # zoom(2)
    
    #pan(-100,-100)
    for obj in screen_objects.obj_list:
        # draw them to the real_space buffer
        for x,y in obj.point_list:
            if x < width and x > 0 and y < height and y > 0:
                real_space[x][y] = obj.color

def zoom(dz):
    scalechange = dz - 1
    offsetX = -(200 * scalechange)
    offsetY = -(200 * scalechange)
    
    for o in screen_objects.obj_list:
        o.translate(offsetX,offsetY)

def pan(dx, dy):
    for obj in screen_objects.obj_list:
        obj.point_list = [(x+dx,y+dy) for x,y in obj.point_list]
            

def real_space_to_pixel_space():
    # TODO
    # So to 'zoom' out maybe we can just decrease the size of everything?
    for x,y in itertools.product(range(width), range(height)):
        pixel = Point(x,y)
        pixel.setFill(real_space[x][y])
        pixel.draw(win)

def main():
    print('Main')
    global win
    win = GraphWin("Graphics Window", width, height, autoflush=False)
    win.setBackground('black')
    draw_function()
    real_space_to_pixel_space()
    win.getMouse()
    win.close()
    print('exited')

if __name__ == '__main__':
    main()
