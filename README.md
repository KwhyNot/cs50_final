## aurora - My cs50 final project

Aurora iteratively takes screenshots of the main screen of the computer, calculates 
the average color values and brightness, and sends that information, via the Hue bridge, 
to one or more Hue bulbs. This allows the user to run Aurora from the terminal, and then 
open up a game or movie and to have the lighting in the room adapt to match the lighting 
present on the screen.

To use Aurora, the user should first open up the file "aurora.py", in a text editor and update
the values of "bridgeIP" and "lightID" to match their equiptment. If unknown, the 
bridge IP address can be found here (as long as the user is connected to the internet 
on the same network as the bridge): https://www.meethue.com/api/nupnp 

The light ids are, by default, integer values from 1 to 3, for the three bulbs included
in the starter kit that comes with the Hue. If more information is necessairy as to how 
to configure Hue bulbs initially, it can be found here: 
http://www.developers.meethue.com/documentation/getting-started

After this, the user should look to the next block comment in "aurora.py" and, per it's
instruction, uncomment the line of code beneath it. This line of code essentially registers
the program with the Hue bridge. The user should save the file and run the program once from 
the terminal (by navigating to the directory containing the program and then running
"python aurora.py" and then terminating the process by ctrl-c). After that, reopen the file 
in a text editor and comment out this line of code again. Now Aurora is ready to go!

Going forward, anytime the user wants to run Aurora while watching a movie or playing a game, 
or even to just have the lights match their content as they browse the web, the user can just 
open up a terminal window, navigate to the directory containing Aurora, and execute 
"python aurora.py". To terminate the process the user can just press ctrl-c and then confirm
that they wish to exit by entering "y".

Enjoy!
