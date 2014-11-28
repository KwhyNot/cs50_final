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