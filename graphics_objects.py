# graphics_objects.py

class group():
    def __init__(self):
        self.obj_list = []

    def add(self, a):
        self.obj_list.append(a)

    def add_multiple(self, obj_list):
        for a in obj_list:
            self.add(a)

    def rm(self, a):
        self.obj_list.remove(a)
    
    def __str__(self):
        return 'Group:'+', '.join(str(a) for a in self.obj_list)

class graphics_object():
    def __init__(self, coords, color=None):
        self.coords = coords
        self.point_list = []
        self.color = 'blue'

    def __str__(self):
        raise NotImplementedError

class point(graphics_object):
    # Not for use in othe grpahics objects
    # Use this when you just want to draw 1 pixel
    def __str__(self):
        return 'point at {}'.format(self.coords)

class line(graphics_object):
    def __init__(self, p1, p2, color = 'blue'):
        self.p1 = p1
        self.p2 = p2
        self.point_list = self.bressenhelm(p1, p2)
        self.color = color
        
    def bressenhelm(self, start, end):
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
            # for i in range(stroke_w):
            # i would be added to y in each
            point = (y, x) if rotated else (x, y)
                # pt(point)
            pts.append(point)
            err -= abs(dy)
            if err < 0:
                y += y_inc
                err += dx

        return pts

    def __str__(self):
        return 'Line from {} to {}'.format(self.p1, self.p2)

class square(graphics_object):
    # super.coords defines the top left corner
    def __init__(self, coords, side_length, color = 'green'):
        self.coords = coords
        self.side_length = side_length
        self.point_list = self.generate_pointlist()
        self.color = color

    # List of points in real space
    def generate_pointlist(self): 
        li = []
        x,y = self.coords # top left
        s = self.side_length
        li.extend(line((x,y),(x+s,y)).point_list) # top
        li.extend(line((x,y),(x,y+s)).point_list)  # left
        li.extend(line((x+s,y),(x+s,y+s)).point_list) # right
        li.extend(line((x,y+s),(x+s,y+s)).point_list) # bottom
        return li

    def __str__(self):
        return 'sqr'

class cirle(graphics_object):
    # super.coords defines the center 
    def __init__(self, coords, radius, color = 'red'):
        self.coords = coords
        self.radius = radius
        self.point_list = self.generate_pointlist()
        self.color = color

    def generate_pointlist(self):
        li = []
        center = self.coords
        r = self.radius
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
                    li.append((x_hat,y_hat))
                    li.append((y_hat,x_hat))
        return li

class polygon(graphics_object):
    def __init__(self, vertex_list, color = 'purple'):
        self.coords = vertex_list[0]
        self.vertex_list = vertex_list
        self.point_list = self.generate_pointlist()
        self.color = color

    def generate_pointlist(self):
        li = []
        verts = self.vertex_list
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
            pts.extend(line(verts[i], verts[i+1]).point_list)
        pts.extend(line(verts[0], verts[-1]).point_list)

        # print(x_min, x_max, y_min, y_max)
        for y in range(y_min, y_max+1):
            passed = 0
            for x in range(x_min, x_max+1):
                if (x,y) in verts:
                    break
                if (x,y) in pts:
                    passed += 1
                elif passed % 2 == 1:
                    li.append((x,y))
        return li




if __name__ == "__main__":
    print('Main Thread')
    my_obj = graphics_object((50,50))
    my_point = point((10,10))
    my_square = square((50,50), 50)
    my_line = line((10,10), (10, 100))
    
    my_group = group()
    my_group.add(my_square)
    my_group.add(my_line)
    print(my_group)
