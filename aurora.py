# -*- coding: utf-8 -*-
"""




"""

""" rgb_cie library from: https://github.com/benknight/
    hue-python-rgb-converter/blob/master/rgb_cie.py
    
    phue library from: https://github.com/studioimaginaire/phue
"""

import signal
import sys
import functions
from phue import Bridge
from rgb_cie import Converter



""" Set the appropriate IP address for your bridge, and specify light ID(s) 
    for whichever lights you want to include.
"""
bridgeIP = "192.168.1.101"
lightID = [1,2,3]
converter = Converter()
bridge = Bridge(bridgeIP)

""" If this is the first time running the program, uncomment the following 
    line, press the button on the bridge and then run the program.
    (this only needs to be run a single time, and then can be commented 
    out again)
"""
# bridge.connect()


""" Iteratively gets rgb values from screenshot(), passes those values to 
    rgbToCIE1931() to calculate the [x, y] color values (formatted for Hue), 
    and passes rgb values to brightness() to get a value for the average 
    brightness. Then passes brightness and color values, along with a transition
    time value, to set_light() which sends that information in a json request
    to the Hue bridge.
"""
def aurora():
    while True: 
        red, green, blue = functions.screenshot()    
        x, y = converter.rgbToCIE1931(red, green, blue)
        bri = int(round(functions.brightness(red, green, blue)))
        command = {'transitiontime' : 4, 'bri' : bri, 'xy' : [x, y]}
        bridge.set_light(lightID, command)
  
 
 
""" Signal handling functions from: http://stackoverflow.com/questions/18114560/
    python-catch-ctrl-c-command-prompt-really-want-to-quit-y-n-resume-executi
"""   
def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nReally quit? (y/n)> ").lower().startswith('y'):
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(1)

    # restore the exit gracefully handler here    
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    aurora()

