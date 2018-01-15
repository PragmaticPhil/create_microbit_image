# create_microbit_image
Simple and quick way to edit and create images for the micro:bit

How To... get it set up:

1 = Load all the files into the same folder somewhere

2 = Open the XLSM

3 = Enable macros

How To... edit an image:

1 = select any cell  in the row with the image you want to edit

2 = click the Edit button

3 = edit your image - click the big tick when you are done.

How To... create a new image:

1 = click the Create Image button

2 = create your image - click the big tick when you are done.

And of course that tantalising micro:bit button!

... this app is not meant to be a create image app - that a byproduct

... one of the things it will do in time is comm over serial to a micro:bit

... but thats not ready and this is a quite nice way to make and edit images.

I left it in as a deliberate tease, of course ;)

And... thanks to @LMcUnderwood for pointing out that you *might* get a FileNotFound error when you run things.
If so, you can fix this by adding a full path for the images "led_ON.jpg" and "led_OFF.jpg" (just those 2 - not for the other 3 images).  Go into the VBA, search for these strings, and replace with the full path.

Thanks!
Philip
