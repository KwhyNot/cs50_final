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


converter = Converter()


""" Set IP address for hub, and specify light ID(s)
"""

# ip = Bridge.get_ip_address()

bridge = Bridge('192.168.1.101')

""" If the app is not registered and the button is not pressed, 
    uncomment the following line, press the button and call connect() 
    (this only needs to be run a single time)
"""
#bridge.connect()



while True:
    red, green, blue = functions.getAverageScreenColor()
    r, g, b = functions.zero_check(red, green, blue)    
    x, y = converter.rgbToCIE1931(r, g, b)
    bri = int(round(functions.gray(r, g, b)))
    command = {'transitiontime' : 4, 'bri' : bri, 'xy' : [x, y]}
    bridge.set_light([1, 2, 3], command)


#b.get_api()



#x, y = functions.rgbConvert(r, g, b)



