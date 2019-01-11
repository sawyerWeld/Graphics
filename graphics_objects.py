# graphics_objects.py
import itertools
import math

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
        self.color = color
    
    def translate(self, dx, dy):
        self.point_list = [(x+dx,y+dy) for (x,y) in self.point_list]

    def top_left_bound(self):
        # Find the top left point in a rectangular bound of the obj
        min_x = min(self.point_list, key=lambda x: x[0])
        min_y = min(self.point_list, key=lambda x: x[1])
        return (min_x[0], min_y[1])

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

        return sorted(pts, key = lambda x: x[1], reverse=True)
        #return pts

    def __str__(self):
        return 'Line from {} to {}'.format(self.p1, self.p2)

class square(graphics_object):
    # super.coords defines the top left corner
    def __init__(self, coords, side_length, color = 'green'):
        self.coords = coords
        self.side_length = side_length
        self.point_list = self.generate_pointlist()
        self.color = color

    def scale(self, scalar):
        self.side_length = math.floor(self.side_length * scalar)
        self.point_list = self.generate_pointlist()

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
    
    def scale(self, d):
        self.radius *= d
        self.point_list = self.generate_pointlist()

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
    def __init__(self, vertex_list, color = 'purple', fill = None):
        self.coords = vertex_list[0]
        self.vertex_list = vertex_list
        if fill == None:
            # Wireframe
            self.color = color
            self.point_list = self.generate_pointlist_nofill()
        else:
            self.border_color = color
            self.color = fill
            self.point_list = self.generate_pointlist()
        self.fill = fill
        
    def scale(self, d):
        self.vertex_list = [(x*d,y*d) for (x,y) in self.vertex_list]
        if self.fill == None:
            self.generate_pointlist_nofill()
        else:
            self.point_list = self.generate_pointlist()


    def get_border(self):
        wireframe = graphics_object([], color = self.border_color)
        wireframe.point_list = self.generate_pointlist_nofill()
        return wireframe

    def generate_pointlist_nofill(self):
        li = []
        verts = self.vertex_list
        pts = []
        for i in range(len(verts)-1):
            pts.extend(line(verts[i], verts[i+1]).point_list)
        pts.extend(line(verts[0], verts[-1]).point_list)
        li = [x for x in pts if x not in verts]
        li.extend(verts)
        # by removing all instances of vertices from the pt list 
        # and then adding them all back in, we ensure that ther
        # is only one instance of each vertex in the list
        return li

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

        # # generate outline
        # pts = self.generate_pointlist_nofill()

        # # fill in the outline
        # for y in range(y_min,y_max+1):
        #     drawing = False
        #     for x in range(x_min, x_max+1):
        #         pt = (x,y)
        #         if pts.count(pt) == 2 or pt in verts:
        #             # This happens when lines oversect
        #             # Like for tight angles
        #             li.append(pt)
        #             continue
        #         if pts.count(pt) == 1:
        #             # this is on 1 line
        #             drawing = not drawing
        #             continue
        #         if drawing == True:
        #             li.append(pt)
        edges = []
        for i in range(len(verts)-1):
            edges.append(line(verts[i], verts[i+1]).point_list)
        edges.append(line(verts[0], verts[-1]).point_list)

        end_points = [(x[0],x[-1]) for x in edges]


        for y in range(y_min,y_max+1):
            # First step is find all the intersections
            # an edge has an intersection one side is below the line
            # and the other side is above the line
            intersecting_edges = []
            for index, pair in enumerate(end_points):
                pt1, pt2 = pair
                if pt1[1] > y and pt2[1] <= y:
                    intersecting_edges.append(index)
            # We've determined which edges we intersect
            # Now find the point of intersection
            # Can there be multiple?
            nodes = []
            for i in intersecting_edges:
                edge = edges[i]
                for pair in edge:
                    _,y_p = pair
                    if y_p == y:
                        nodes.append(pair)
                        continue
            # sort by x value
            nodes.sort(key = lambda x: x[0])
            pairs = [(nodes[i],nodes[i+1]) for i in range(0,len(nodes),2)]
            for pair in pairs:
                pt1,pt2 = pair
                x1 = pt1[0]
                x2 = pt2[0]
                x_values = list(range(x1,x2+1))
                segment = [(x,y) for x in x_values]
                li.extend(segment)
                

            # for x in range(x_min, x_max+1):
            #     pt = (x,y)
            #     # if there are an odd number of intersections on each side, etc
                
        
        
        # li.extend(pts)
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
