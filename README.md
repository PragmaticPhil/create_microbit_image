
# create_microbit_image

Simple and quick way to edit and create images and animations (up to 10 frames) for the micro:bit.

An easy UI allows you to create images / animations quickly, and outputs Python code for you to use in your apps.

You can also 'fling' your images / animations onto a micro:bit that is connected over serial.  Its quite cool, tbh!

Read INSTALL_INSTRUCTIONS to get it onto your machine.

NB:

This works with Excel16 (desktop version) running on Win10.  I have no means to test on other setups.

----------------------------------------------------

With the App you can do the following:

## IMAGES:

Create and edit images for the micro:bit 5x5 LED matrix (screen).

Send these images over serial to a connected micro:bit to review them (micro:bit must be running the supplied code)

Copy and paste the Python and Image code to use in your applications.


## ANIMATIONS:

Create and edit animations of up to 10 frames.

Use images you have created to construct these animations.

Review the animations in-app or on your connected micro:bit (micro:bit must be running the supplied code)

Copy the Python code - a full and working .py is generated with the animation.


-----------------------------------------------------

## ATRRIBUTIONS

... don't blame anyone below for any flaws - they pointed me at things I needed, and they bear no culpability for what I did with them!!!

... https://github.com/fizban99/microbit_us100/blob/master/us100.py - the first decent example of a uart read I found for micro:bit running microPython.

... Carlospherate - a colleague who pointed me out of a dark corner.

... Yigal Edery - a VBA master.  Without his help (esp the COM port numbering issue and his brilliant Life game) I wouldn't have had a chance!  And his excellent blog [] first made me realise that a link between Exvel and micro:bit was feasible.

... @LMcUnderwood for testing several iterations and identifying a bunch of bugs.  Also for challenging me to add in new functionality that helps with UX (esp the preview capabilities in the animation form.

----------------------------------------------------


Thanks!
Philip M (PragmaticPhil)
