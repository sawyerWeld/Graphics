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

gm.run_drawing(setup_function = setup, draw_function = draw)
