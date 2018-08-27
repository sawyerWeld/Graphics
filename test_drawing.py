import graphics_minimal as gm

def setup():
    gm.set_dimensions(250,500)
    back = gm.color_rgb(100, 0 , 255)
    gm.set_background(back)

def draw():
    gm.pt(50, 50)
    gm.col('red')
    gm.pt(200, 250)
    gm.col('blue')
    gm.pt(50, 100)
    gm.col('red')
    gm.rect(50,50,50,50)

def rect(x, y, w, h):
    for i in range(h):
        for j in range(w):
            gm.pt(x+j, y+i)

gm.run_drawing(setup_function = setup, draw_function = draw)
