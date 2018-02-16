from microbit import *

# We'll set up a simple String buffer that can carry 10 images (for previewing animations).
global imageDataStore 
imageDataStore = ["", "", "", "", "", "", "", "", "", ""]

# We will read each row into an array as they are received:
global rawImageStrData
rawImageStrData = ["", "", "", "", ""]

#   Because we read in 1 row at a time, there is a risk of having all 5 rows, but some being for the wrong frame...
#   So, we record the frame that each row is associated with:
#global rawImageDataFrameIDs
#rawImageDataFrameIDs = [0, 0, 0, 0, 0]
#   NB - this is turned off for now@
#   each image in an animation has to be processed within 1 second (delay coded into the Excel) and this code seems to take too long to run.
#   So, sometimes we end up with rows from previous images, but incidence is low and this will be fixed next version

#   The method used to read from the UART buffer is that we read 1 char at a time... for iteration 2 I am working on a more efficient method.
#   But, for now we read chars in the buffer until we come to a 'X', which denotes the beginning of data containing a row of image data.
#   we use a switch - when an active row is detected (i.e. 'X' is detected) we turn it True and read the next 7 chars into bufStrFromUSB.
global activeRow
activeRow = False

#   As we read valid chars from the UART buffer we add them to this string, which is processed when it reaches 8 chars in length.
global bufStrFromUSB
bufStrFromUSB = ""
#   There is more info on how the comm protocol works here: https://github.com/PragmaticPhil/create_microbit_image/blob/master/Communication%20Protocol

global BAUD_Rate
BAUD_Rate = 11520       #   Rem to ensure Excel is set with same value.

global runInit          #   A switch so we can run some code on startup
runInit = True


def getComm():
    try:
        uart.init(baudrate=BAUD_Rate, bits=8, parity=None, stop=1)
        #sleep(1)                   #  can't quite decide if this helps marginally (with the success rate of the COM comm) or not.
                                    #  ... the way I read the buffer means these 1s add up though, so unless I can see a need its out for now.
        buf = bytearray(1)          #  Not an ideal method - read one char at a time... very slow.  First iteration only (built from POC code)
        
        if(uart.any()):             #  Note - a brief sleep here would expeditious - to let the write complete and the buffer fill up...
                                    #  except that we read the array 1 char at a time, so not really necessary.
            uart.readinto(buf, 1)   #  reads 1 char from the USB / UART buffer into our bytearray buffer
        return(buf[0])

    except:
        uart.init(BAUD_Rate)


def getImageDataFromUSB():          #   Called by main each cycle, this checks buffer and processes it 1 char at a time.
    global activeRow
    global bufStrFromUSB            #   Global cos we pass through this a single char at a time and add to this buffer
    
    intBuf = getComm()              #   get the next single char in the UART buffer.
        
    #   Rule: first char of a target comm (a row of image data) mus be 'X' - ASCII = 88
    if(intBuf == 88):               #   initialise a new raw row record:
        activeRow = True            #   This switch means that this and the next 7 chars to be read will be added to the str buffer
        bufStrFromUSB = "X"         #   Not really necessary - we could dispense with this - its first iteration (POC) code.

    #   Rule: all information carrying data is encoded in integers values - we are not interested in other chars:
    if(activeRow):
        if(intBuf > 47 and intBuf < 58):                        # we are only interested in integers - we consume all other data.
            bufStrFromUSB = bufStrFromUSB + str(chr(intBuf))

    #   Rule: a valid image record row will have 8, no more, no less, chars.
    if (len(bufStrFromUSB) == 8):
        activeRow = False                       #   we have received the full row of data - no need to process more.
        processRawRowData(bufStrFromUSB)        #   so we send the string to be processed


def processRawRowData(rawRowStr):               #   takes an 8 char string and extracts row data, which is saved in rawImageStrData[rowID]
    #global rawImageDataFrameIDs                #   hidden cos it slows down things too much :(
    try:
        frameID = int(rawRowStr[1])
        rowID = int(rawRowStr[2])
        #rawImageDataFrameIDs[rowID] = frameID      #   hidden - introduces performance issues with animations.  Will fix in next version.
        rawImageData = str(rawRowStr[3:8])          #   the 5 values for the row are encoded in this part of the string.
        if(not(rowID  == 4)):
            rawImageData = rawImageData  +":"       #   getting ':' added now (row separator) so we can make image str easily later on.
        rawImageStrData[rowID] = rawImageData       #   row data has been extracted and added to the buffer
        checkAndFinaliseImage(frameID)              #   now we check if we have enough data (5 full rows) to make an image
        return
    except:
        return


def checkAndFinaliseImage(frameID):                 #   is there adequate info in rawImageStrData to make an image?  If so, display it.
    global imageDataStore
    global rawImageStrData

    # we will check if all data for the current frame has been received - if so we'll add it to the imageID frame:
    #if(checkImageIsReady()):
    allImageData = ""           #   we are ready to concatenate the raw row data into an image string
    for i in range(0, 5):
        if(len(rawImageStrData[i]) < 5):    return              #   bails if any of the rows are incomplete.
        allImageData  = allImageData  + rawImageStrData[i]

    imageDataStore[frameID] = allImageData
    display.show(Image(imageDataStore[frameID]))
    #rawImageStrData = ["", "", "", "", ""]         
    #   ... above is the logical thing to do.  BUT - turning this on slows down animations too much.  It also
    #   removes a cool effect - the image visually updating row-by-row.


def checkImageIsReady():                    #   Not used - introduces performance issues.  Left in for next iteration
    global rawImageStrData
    higestFrameIndex = 0                    #   we need to ensure all 5 components (rows) belong to the same frame, and the correct (latest) one
    
    imageBufferIsReady = True
    for i in range(0, 5):
        if(len(rawImageStrData[i]) < 5): 
            imageBufferIsReady = False
        #else:
        #    if(rawImageDataFrameIDs[i] > higestFrameIndex): higestFrameIndex = rawImageDataFrameIDs[i]
    return imageBufferIsReady
    #   Code below ensure image refreshes crisply with no rows from previous frame... but runs too slow and causes issues
    #   with animations (dropping frames).  Leaving it in for now in case i can increase processing time elsewhere.
    #if(higestFrameIndex == 0): return imageBufferIsReady

    #for i in range(0, 5):
    #    if(not( rawImageDataFrameIDs[i] == higestFrameIndex)):
    #       imageBufferIsReady = False
    #       rawImageStrData[i] = ""
    #return imageBufferIsReady


def initMethod():
    global runInit
    display.show(Image("90900:09090:90990:00090:00099"))    #   ex:bit logo - shown on startup
    runInit = False


while True:
    if(runInit): initMethod()
    getImageDataFromUSB()

    if(button_a.was_pressed()):                             #   Show image in buffer 0 for 1 second
        display.show(Image((imageDataStore[0])))
        sleep(1000)

    if(button_b.was_pressed()):                             #   Show all buffers with half second delay.
        for i in range (0, 10):
            display.show(Image((imageDataStore[i])))
            sleep(500)