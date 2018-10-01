import graphics_minimal as gm

class Rectangle:
    
    def __init__(self, x, y, w, h):
            self.x = x
            self.y = y
            self.w = w
            self.h = w

    def draw(self):
        for i in range(self.h):
            for j in range(self.w):
                gm.pt((self.x+j, self.y+i))

class Square:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def draw(self):
        x = self.x
        y = self.y
        r = self.r
        gm.line((x,y),(x+r,y))
        gm.line((x+r,y),(x+r,y+r))
        gm.line((x+r,y+r),(x,y+r))
        gm.line((x,y+r),(x,y))