# -*- coding: utf-8 -*-
"""
Created on Fri Nov 21 19:50:33 2014

@author: christophermurphy
"""

import os
import tempfile
from PIL import Image
from subprocess import call


def screenshot():   
    tf = tempfile.NamedTemporaryFile(suffix='.png')  
    print tf.name  # retrieve the name of the temp file just created
    call(["screencapture", "-x", tf.name])
    screen = Image.open(tf.name)
    red, green, blue = averageRGB(screen)
    red, green, blue = zero_check(red, green, blue)
#    os.remove("screenshot.png")
    return red, green, blue      
    
"""    
    call(["screencapture", "-x", "screenshot.png"]) 
    screen = Image.open("screenshot.png")
"""
      


def averageRGB(screen):  
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
    return red, green, blue
    
    
def zero_check(red, green, blue):
    if red + green + blue < 0.001:
        red = 0.001
        green = 0.001 
        blue = 0.001
    return red, green, blue


""" Formula for brightness found here: 
    http://en.wikipedia.org/wiki/Luma_(video)
"""
def brightness(red, green, blue):
    brightness = 0.2126*red + 0.7152*green + 0.0722*blue
    return brightness



"""

# sRGB luminance(Y) values
rY = 0.212655
gY = 0.715158
bY = 0.072187

# Inverse of sRGB "gamma" function. (approx 2.2)
def inv_gam_sRGB(ic):
    c = ic/255.0
    if ( c <= 0.04045 ):
        return c/12.92
    else: 
        return pow(((c+0.055)/(1.055)),2.4)

# sRGB "gamma" function (approx 2.2)
def gam_sRGB(v):
    if(v<=0.0031308):
        v *= 12.92
    else: 
        v = 1.055*pow(v,1.0/2.4)-0.055
    return (v*255+.5)

# GRAY VALUE ("brightness")
def gray(r, g, b): 
    return gam_sRGB(
            rY*inv_gam_sRGB(r) +
            gY*inv_gam_sRGB(g) +
            bY*inv_gam_sRGB(b)
    )
"""





""" 
def rgbConvert(r, g, b):
    
    Calculates the XY values (in the Hue format) from RGB values.
    Returns the X and Y values of the color, as floats.
  
    r = pow((r + 0.055) / (1.0 + 0.055), 2.4) if r > 0.04045 else r / 12.92
    g = pow((g + 0.055) / (1.0 + 0.055), 2.4) if g > 0.04045 else g / 12.92
    b = pow((b + 0.055) / (1.0 + 0.055), 2.4) if b > 0.04045 else b / 12.92
    X = r * 0.649926 + g * 0.103455 + b * 0.197109
    Y = r * 0.234327 + g * 0.743075 + b * 0.022598
    Z = r * 0.000000 + g * 0.053077 + b * 1.035763
    x = X / (X + Y + Z)
    y = Y / (X + Y + Z)
    return x, y
"""    

