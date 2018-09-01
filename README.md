# Graphics
Creating a raster graphics library from just one function

Current features:
col(color)
	Changes to current color to draw with. If no color argument is passed
	to an object it defaults to whatever color col() was last called with.
pt(x, y)
	Paints the pixel at position (x,y)
rect(x, y, w, h)
	Fills a rectangle with top-left corner(x,y) with width w and height h
	Todo add fill and outline to be seperate entities
	That feature may be implemented when I get to polygonal fills
line(x0,y0,x1,y1)
	Draws a line from (x0,y0) to (x1,y1)
	Currently implementing changes for this
	Special case for vertical lines because slope = 0 caused divide by 0

Currently implementing:
pen thickness, styles, antialiasing for line()

Currently thinking about:
Real space vs. pixel space. I think I need to store a global transition matrix that maps from the first to the later. 

How to test features robustly. I think I may implement a 2d array as a screen buffer that is created when I call the createwindow method and written to when i call the pt() method.
