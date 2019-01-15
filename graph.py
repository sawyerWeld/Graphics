from graphics import *
import graphics_objects as g
import itertools
import copy
import pickle

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

def put_txt(coords, message, color = 'white'):
    global cur_color
    cur_color = color
    obj = g.text(coords, message, color)
    screen_objects.add(obj)

def draw_function():
    
    # This is where you can programmatically interact
    crl = g.circle((50,50),10,'blue')
    
    put_txt((10,380),'Drawn programmatically with function','yellow')
    
    screen_objects.add_multiple([crl])

# dont use
def zoom(dz):
    scalechange = dz - 1
    offsetX = -(200 * scalechange)
    offsetY = -(200 * scalechange)
    
    for o in screen_objects.obj_list:
        o.translate(offsetX,offsetY)

def pan(dx, dy):
    # TODO test
    for obj in screen_objects.obj_list:
        obj.translate(-dx,-dy)
            

def real_space_to_pixel_space():

    for obj in screen_objects.obj_list:
        # draw them to the real_space buffer
        for x,y in obj.point_list:
            if x < width and x > 0 and y < height and y > 0:
                real_space[x][y] = obj.color

    for x,y in itertools.product(range(width), range(height)):
        pixel = Point(x,y)
        pixel.setFill(real_space[x][y])
        pixel.draw(win)


def read_file(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    obj_count = 0
    group_count = 0
    file_items = []
    for l in lines:
        
        line = l.split()
        
        func = None
        command = None
        func_name = line[0]
        
        color = None
        # basic shapes
        color_string = ''

        if func_name == 'sqr':
            obj_count += 1
            coords = line[1]
            side_len = line[2]
            
            if len(line) > 3:
                color = line[3]
                color_string = ',\'{}\''.format(color)
            command = 'obj{} = g.square({},{}{})'.format(obj_count,coords,side_len,color_string)
            
            exec(command)
            exec('file_items.append(obj{})'.format(obj_count))

        elif func_name == 'ply':
            obj_count += 1
            vertex_list = []

            fill_string = ''

            fill = False
            color_specified = False

            if line[-1] == 'fill':
                line.pop()
                fill = True

            for token in line[1:]:
                if token[0] == '(':
                    # we have a vertex here
                    exec('vertex_list.append({})'.format(token))
                else:
                    color_string = ',\'{}\''.format(token)
                    color_specified = True
            
            fill_string = ',{}'.format(fill)

            if color_specified == False and fill == False:
                command = 'obj{} = g.polygon(vertex_list)'.format(obj_count)  
            elif color_specified == True and fill == False:
                command = 'obj{} = g.polygon(vertex_list{})'.format(obj_count,color_string)
            elif color_specified == False and fill == True:
                command = 'obj{} = g.polygon(vertex_list,fill=True)'.format(obj_count)
            else:
                command = 'obj{} = g.polygon(vertex_list{},fill=True)'.format(obj_count,color_string,fill_string)
            exec(command)
            exec('file_items.append(obj{})'.format(obj_count))

        elif func_name == 'crl':
            obj_count += 1
            coords = line[1]
            radius = line[2]

            if len(line) > 3:
                color = line[3]
                color_string = ',\'{}\''.format(color)
            command = 'obj{} = g.circle({},{}{})'.format(obj_count,coords,radius,color_string)
           
            exec(command)
            exec('file_items.append(obj{})'.format(obj_count))

        elif func_name == 'lin':
            obj_count += 1
            pt1 = line[1]
            pt2 = line[2]

            if len(line) > 3:
                color = line[3]
                color_string = ',\'{}\''.format(color)

            command = 'obj{} = g.line({},{}{})'.format(obj_count,pt1,pt2,color_string)
            
            exec(command)
            exec('file_items.append(obj{})'.format(obj_count))

        # group command
        elif func_name == 'grp':
            group_count += 1
            command = 'grp{} = g.group()'.format(group_count)
            exec(command)
            for token in line[1:]:
                command = 'grp{}.add(obj{})'.format(group_count,token[-1])
                exec(command)

        elif func_name == 'rot':
            focus_string = ''
            if len(line) > 3:
                # focus point specified
                focus_string = ',{}'.format(line[3])
            command = '{}.rotate({}{})'.format(line[1],line[2],focus_string)
            
            exec(command)

        elif func_name == 'tra':
            command = '{}.translate({},{})'.format(line[1],line[2],line[3])
            
            exec(command)

        elif func_name == 'scl':
            command = '{}.scale({})'.format(line[1],line[2])
            
            exec(command)

        elif func_name == 'txt':
            coords = line[1]
            message = '\'{}\''.format(line[2].replace('_',' '))
            if len(line) > 3:
                color = line[3]
                color_string = ',\'{}\''.format(color)
            command = 'put_txt({},{}{})'.format(coords, message, color_string)
            exec(command)

        elif func_name == 'sav':
            save(filename = line[1])

        elif func_name == 'lod':
            load(filename = line[1])

    return file_items

def save(filename):
    filename = "data_files/{}.p".format(filename)
    pickle.dump(screen_objects.obj_list, open(filename, 'wb'))
    print('Saved to {}'.format(filename))

def load(filename):
    filename = 'data_files/{}.p'.format(filename)
    file_objects = pickle.load(open(filename,'rb'))
    screen_objects.add_multiple(file_objects)
    print('Loaded {} graphics objects from file {}'.format(len(file_objects),filename))
    for f_o in file_objects:
        print()

def main():
    global win
    win = GraphWin("Graphics Window", width, height, autoflush=False)
    win.setBackground('grey')
    if len(sys.argv) == 2:
        input_objects = read_file(sys.argv[1])
        screen_objects.add_multiple(input_objects)
    else:
        draw_function()
    real_space_to_pixel_space()
    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
