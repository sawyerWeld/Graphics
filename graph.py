from graphics import *
import graphics_objects as g
import itertools

# Redoing graphics because it became a software engineering mess
win = None # have to have this at global level to use zelle graphics
width = 400
height = 400
real_space =  [[ 'black' for j in range(width)] for i in range(height)]
cur_color = 'green'
zoom_level = 400 # zoom at 400, 200, 100?
screen_objects = g.group() # the objects we want displayed

def pt(coords):
    x,y = coords
    real_space[x][y] = cur_color

def draw_function():
    pt((10,10))
    my_line = g.line((10,10), (10, 100))
    my_square = g.square((200,200),50)
    cr1 = g.cirle((100,100),100)
    ply1 = g.polygon([(10,10),(50,50),(20,200)])
    screen_objects.add_multiple([my_line, my_square, cr1, ply1])

    for obj in screen_objects.obj_list:
        # add draw them to the real_space buffer
        for x,y in obj.point_list:
                real_space[x][y] = obj.color
        pass

def real_space_to_pixel_space():
    # TODO
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
