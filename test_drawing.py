import graphics_minimal as gm
width = 5
height = 5


def setup():
    gm.set_dimensions(width, height)
    back = gm.color_rgb(100, 0 , 255)
    gm.set_background('black')

def draw():
    gm.col('red')
    test_grids(mode = 1)
    gm.col('white')
    print(gm.testing_buffer)

def test_grids(mode = 0, inc = 50):
    h = 0
    while h < height:
        gm.line((0,h),(width,h))
        h += inc
    w = 0
    while w < width:
        gm.line((w,0),(w,height))
        w += inc

def rect(x, y, w, h):
    for i in range(h):
        for j in range(w):
            gm.pt(x+j, y+i)

gm.run_drawing(setup_function = setup, draw_function = draw)
