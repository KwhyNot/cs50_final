# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 13:31:06 2014

@author: christophermurphy
"""

#import json
import functions

""" Library from: https://github.com/benknight/hue-python-rgb-converter/
    blob/master/rgb_cie.py
"""
from rgb_cie import Converter
converter = Converter()


""" Set IP address for hub, and specify light ID(s)
"""
hubIP = "192.168.1.101"
lightID = 1


#while True:
r, g, b = functions.getAverageScreenColor()
x, y = converter.rgbToCIE1931(r, g, b)
bri = int(round(functions.gray(r, g, b)))

print (r, g, b)
print (x, y)
print (bri)
#x, y = functions.rgbConvert(r, g, b)



