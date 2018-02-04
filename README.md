  
# create_microbit_image

Simple and quick way to edit and create images and animations (up to 10 frames) for the micro:bit.

An easy UI allows you to create images / animations quickly, and outputs Python code for you to use in your apps.

You can also 'fling' your images / animations onto a micro:bit that is connected over serial.  Its quite cool, tbh!

Read INSTALL_INSTRUCTIONS to get it onto your machine.

NB:

This works with Excel16 (desktop version) running on Win10.  I have no means to test on other setups.

----------------------------------------------------

### IMAGES:

Create and edit images for the micro:bit 5x5 LED matrix (screen) in an easy to use UI in exbit in Excel.

Send these images over serial to a connected micro:bit to review them (NB: micro:bit must be running the supplied code)

Copy and paste the Python and Image code to use in your applications.

----------------------------------------------------

### ANIMATIONS:

Create and edit animations of up to 10 frames.

Use images you have created to construct these animations.

Review the animations in-app or on your connected micro:bit (micro:bit must be running the supplied code)

Copy the Python code - a full and working .py is generated with the animation :)

-----------------------------------------------------

### ATTRIBUTIONS

... don't blame anyone below for any flaws - they pointed me at things I needed, and they bear no culpability for what I did with them!!!

... https://github.com/fizban99/microbit_us100/blob/master/us100.py - the first decent example of a uart read I found for micro:bit running microPython that actually worked for me.  Best Eureka moment for ages, thanks :)

... Carlospherate - a colleague and well known micro:bit maestro who pointed me out of a dark corner.  Twice!

... Yigal Edery - a VBA master.  Without his help (esp the COM port numbering issue and his brilliant Life game) I wouldn't have had a chance!  And his excellent blog (URL below) first showed me how a link between Excel and micro:bit was feasible.

https://techcommunity.microsoft.com/t5/Excel-Blog/Excel-and-Micro-Bit-Hacking-for-fun-and-creativity/ba-p/63603

... @LMcUnderwood for testing several iterations and identifying a bunch of bugs and UX fails.  Also for challenging me to add in new functionality that helps with UX (esp the preview capabilities in the animation form).

----------------------------------------------------

### NEXT:

I built this as a POC to see if Excel could be used to power my matrix (https://twitter.com/pragmaticPhil/status/932333941440352256).

I have learned:

... the method I am using to read data in Python is probably inefficient - I keep reading the buffer until the whole message has been sent.  For the matrix I need shorter messsages and a confirm routine.

... exbit will be a great way to 'program' the matrix (set up different nodes to play different animations / scroll), but needs a lot of speeding up to control in real time.

So exbit is not really a thing - it will become the matrix:bit server, or something.  However, I have grown quite fond of exbit - it really is fun creating images on screen and viewing them.  I am tempted to add in new features - any ideas???



Thanks!

Philip M (PragmaticPhil)
