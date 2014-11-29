# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 19:50:33 2014

@author: christophermurphy
"""
from PIL import Image
import os

def getAverageScreenColor():   
    from subprocess import call
    call(["screencapture", "-x", "screenshot.png"]) 
    screen = Image.open("screenshot.png")   
    left, top, width, height = screen.getbbox()
    red, green, blue = 0.0, 0.0, 0.0
    for y in range(0, height, 8):
        for x in range(0, width, 8):
            color = screen.getpixel((x, y))
            red += color[0]
            green += color[1]
            blue += color[2]
    total = y/8 * x/8
    if red != 0:
        red /= total
    if blue != 0:
        blue /= total
    if green != 0:
        green /= total
    os.remove("screenshot.png")
    return red, green, blue
 
def rgbConvert(r, g, b):
    """ Calculates the XY values (in the Hue format) from RGB values.
        Returns the X and Y values of the color, as floats.
    """
    r = pow((r + 0.055) / (1.0 + 0.055), 2.4) if r > 0.04045 else r / 12.92
    g = pow((g + 0.055) / (1.0 + 0.055), 2.4) if g > 0.04045 else g / 12.92
    b = pow((b + 0.055) / (1.0 + 0.055), 2.4) if b > 0.04045 else b / 12.92
    X = r * 0.649926 + g * 0.103455 + b * 0.197109
    Y = r * 0.234327 + g * 0.743075 + b * 0.022598
    Z = r * 0.000000 + g * 0.053077 + b * 1.035763
    x = X / (X + Y + Z)
    y = Y / (X + Y + Z)
    return x, y
    
r, g, b = getAverageScreenColor()
print (r, g, b)
x, y = rgbConvert(r, g, b)
print (x, y)

