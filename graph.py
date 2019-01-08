from graphics import *

# Redoing graphics because it became a software engineering mess
width = 400
height = 400
real_space =  [[ None for j in range(width)] for i in range(height)]
zoom_level = 400 # zoom at 400, 200, 100?

def draw_function():
    pass

def main():
    print('Main')
    global win
    win = GraphWin("Graphics Window", width, height, autoflush=False)
    win.setBackground('black')
    draw_function()
    win.getMouse()
    win.close()
    print('exited')

if __name__ == '__main__':
    main()
