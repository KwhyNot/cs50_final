# -*- coding: utf-8 -*-
"""
Christopher Murphy

"""

import os
#import tempfile
from PIL import Image
from subprocess import call


""" Captures a screenshot, passes the image to 
    to subsequent functions for processing, and then
    deletes the screenshot.
"""
def screenshot():   
    call(["screencapture", "-x", "screenshot.png"]) 
    screen = Image.open("screenshot.png")    
    red, green, blue = averageRGB(screen)    
    red, green, blue = zero_check(red, green, blue)
    os.remove("screenshot.png")
    return red, green, blue      
    


""" tf = tempfile.NamedTemporaryFile(suffix='.png')  
    call(["screencapture", "-x", tf.name])
    screen = Image.open(tf.name)    
"""

""" Calculates the average value of red, green, and blue
    pixels in the image. Based on the getAverageScreenColor
    function found here: https://github.com/crummy/ambihue/
    blob/master/ambihue.py
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

    
""" Checks if the sum is equal to 0 and, if that is the case,
    reassigns the values to a close approximation. Done to avoid a float 
    division by 0 error when the values are passed to rgbToCIE1931.
"""    
def zero_check(red, green, blue):
    if red + green + blue < 0.001:
        red = 0.001
        green = 0.001 
        blue = 0.001
    return red, green, blue


""" Calculates an average value for brightness in the image.
    Formula for brightness found here: 
    http://en.wikipedia.org/wiki/Luma_(video)
"""
def brightness(red, green, blue):
    brightness = 0.2126*red + 0.7152*green + 0.0722*blue
    return brightness

