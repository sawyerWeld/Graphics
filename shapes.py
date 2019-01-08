import graphics_minimal as gm

obj_list = []

def translation(dx = 0, dy = 0, dz = 0):
    for obj in obj_list:
        obj.changeX(dx)
        print(obj.x)
        # move the points
        for (x,y) in obj.points:
            x += dx
            y += dy
    

def draw_all():
    for obj in obj_list:
        obj.draw()


class Shape:
    x = 0
    y = 0

    points = []

    def changeX(self, dx):
        self.x += dx

    def draw(self):
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
                self.points.append((self.x+j, self.y+i))
        for pt in self.points:
            gm.pt(pt)

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

class Circle(Shape):

    def __init__(self, x, y ,r):
        self.x = x
        self.y = y
        self.r = r
        obj_list.append(self)

    def draw(self):
        center = (self.x, self.y)
        r = self.r

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
                    gm.pt((x_hat,y_hat))
                    gm.pt((y_hat,x_hat))

def polygon_fill(*args):
    verts = list(args)
    # print(verts)
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

    # print(x_min, x_max, y_min, y_max)
    for y in range(y_min, y_max+1):
        passed = 0
        for x in range(x_min, x_max+1):
            if (x,y) in verts:
                break
            if (x,y) in pts:
                passed += 1
            elif passed % 2 == 1:
                gm.pt((x,y))