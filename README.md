
# create_microbit_image
Simple and quick way to edit and create images and animations (up to 10 frames) for the micro:bit

You can also 'fling' your images onto a micro:bit that is connected over serial.  Its quite cool, tbh!

----------------------------------------------------

To enable a micro:bit to communicate over a serial / USB / UART / COM:

1 = you will need to have the MBed Serial Driver for micro:bit installed - google will help.  If you can use REPL in Mu then you already have it.

2 = Find the number of the COM port associated with micro:bit

NB - IF the COM port number is too high EXCEL DOES NOT HANDLE IT - idk why, but debugging that was fun (thanks Yigal!).  Change it to a single digit COM port if you want this to work.

That SHOULD be enough - depends on lot on OS and pure luck, I guess.  Worked for me on Win10 is all I can attest to.

----------------------------------------------------

How To... 'install' the spreadsheet:

1 = Load all the files into the same folder somewhere

2 = Open the XLSM

3 = Enable macros

----------------------------------------------------

How To... edit an image:

1 = select any cell  in the row with the image you want to edit

2 = click the Edit button

3 = edit your image - click the big tick when you are done.

----------------------------------------------------

How To... create a new image:

1 = click the Create Image button

2 = create your image - click the big tick when you are done.

----------------------------------------------------

How To... fling the image to the micro:bit:

Click the micro:bit button in the image editor.

NB - do YOU like pushing the button in a lift to speed it up?  If so, you'll love this... the 'app' (what should I call it) can get a bit confused at times - if you push the micro:bit button once and it doesn't work then KEEP PUSHING IT UNTIL IT DOES.  Seriously!  I will debug it, but I found clicking the button multiple times to be quite therapuetic!

----------------------------------------------------

So - usually the image should transfer quite quickly - a second, more or less.  If you are sitting there 3 seconds later and no image then clickety click away!  Longest it has taken AND STILL WORKED is 16 seconds.  I reckon if you've had nothing after 20 seconds, and you've tried resetting your micro:bit, then summat is wrong.  I might be able to help if you are on Win10 - probs best to get yourself a terminal emulator to check that your com ports are operating.

----------------------------------------------------

BUGS:
... IF your micro:bit is NOT plugged in and you click the Fling button you will see an unhandled error - either cancel the VBA error message or go and check it out

If you check the code you will notice that error trapping is commented out.  DO NOT UNCOMMENT THE ERROR TRAPPING - every time I run it with that error code enabled and the micro:bit not plugged in it crashes Excel.  Better a VBA error you can cancel than a fatal error that will crash Excel.

----------------------------------------------------

Some attributions... don't blame anyone below for any flaws - they pointed me at things I needed, and they bear no culpability for what I did with them!!!

... https://github.com/fizban99/microbit_us100/blob/master/us100.py - the first decent example of a uart read I found for micro:bit running microPython.

... Carlospherate - a colleague who pointed me out of a dark corner.

... Yigal Edery - a VBA master.  Without his help (esp the COM port numbering issue and his brilliant Life game) I wouldn't have had a chance!  And his excellent blog [] first made me realise that a link between Exvel and micro:bit was feasible.

And also thanks to @LMcUnderwood for pointing out a 'bug' (OK Lorainne - a bug not a 'bug' ;) in the original version I uploaded (image not found).

----------------------------------------------------

DISCLAIMER:

This really is dirty code - totally first iteration in a number of places.  I'd usually refactor it to death, but tbh I am just dead chuffed to get this working - I really like it!  My VBA is especially crappy - children - don't do it like that at home ;)

Thanks!
Philip
