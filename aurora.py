# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 13:31:06 2014

@author: christophermurphy
"""

""" rgb_cie library from: https://github.com/benknight/
    hue-python-rgb-converter/blob/master/rgb_cie.py
    
    phue library from: https://github.com/studioimaginaire/phue
"""
import functions
#import phue
from phue import Bridge
from rgb_cie import Converter



""" Set IP address for bridge, and specify light ID(s)
"""
bridgeIP = "192.168.1.101"
lightID = [1, 2, 3]


converter = Converter()
bridge = Bridge(bridgeIP)

""" If the app is not registered and the button is not pressed, 
    uncomment the following line, press the button and call connect() 
    (this only needs to be run a single time)
"""
# bridge.connect()



while True:
    red, green, blue = functions.screenshot()    
    x, y = converter.rgbToCIE1931(red, green, blue)
    bri = int(round(functions.brightness(red, green, blue)))
#command = {'transitiontime' : 4, 'bri' : bri, 'xy' : [x, y]}
#bridge.set_light(lightID, command)



#x, y = functions.rgbConvert(r, g, b)



