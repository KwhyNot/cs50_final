
import functions
#import phue
from phue import Bridge
from rgb_cie import Converter
import tempfile
import os
from PIL import Image
from subprocess import call


tf = tempfile.NamedTemporaryFile(suffix='.png')  
print tf.name  # retrieve the name of the temp file just created
call(["screencapture", "-x", tf.name])
screen = Image.open(tf.name)
red, green, blue = averageRGB(screen)
red, green, blue = zero_check(red, green, blue)
print red, green, blue   


#screen = screenshot()