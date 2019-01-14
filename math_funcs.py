# Math helper functions
import math

# Rotation about a point

def rotate(point, degrees, focus = (0,0)):
    x_focus, y_focus = focus
    x_point, y_point = point
    theta = math.radians(degrees)
    x_result = x_focus + math.cos(theta) * (x_point - x_focus) - math.sin(theta) * (y_point - y_focus)
    y_result = y_focus + math.sin(theta) * (x_point - x_focus) + math.cos(theta) * (y_point - y_focus)
    return (x_result, y_result)
    

