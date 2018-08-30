import graphics_minimal as gm

def setup():
    gm.set_dimensions(250,500)
    back = gm.color_rgb(100, 0 , 255)
    gm.set_background('black')

def draw():
    gm.col('white')
    gm.line(0,400,200,100)

def rect(x, y, w, h):
    for i in range(h):
        for j in range(w):
            gm.pt(x+j, y+i)

gm.run_drawing(setup_function = setup, draw_function = draw)
