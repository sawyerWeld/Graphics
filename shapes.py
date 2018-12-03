import graphics_minimal as gm

obj_list = []

def translation(dx = 0, dy = 0, dz = 0):
    for obj in obj_list:
        obj.changeX(dx)
        print(obj.x)

def draw_all():
    for obj in obj_list:
        obj.draw()


class Shape:
    def changeX(self, dx):
        self.x += dx

    def draw():
        pass


class Rectangle(Shape):
    
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = w
        obj_list.append(self)
        

    def draw(self):
        for i in range(self.h):
            for j in range(self.w):
                gm.pt((self.x+j, self.y+i))

class Square(Shape):

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        obj_list.append(self)

    def draw(self):
        x = self.x
        y = self.y
        r = self.r
        gm.line((x,y),(x+r,y))
        gm.line((x+r,y),(x+r,y+r))
        gm.line((x+r,y+r),(x,y+r))
        gm.line((x,y+r),(x,y))