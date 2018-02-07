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

# we use a switch - when an active row is detected (i.e. metadata from serial comms indicates beginning of image data) we turn it True and read into bufStrFromUSB.
global activeRow
activeRow = False
#   As we read valid chars from the buffer we add them to this string, which is processed when it reaches 8 chars in length.
global bufStrFromUSB
bufStrFromUSB = ""

global BAUD_Rate
BAUD_Rate = 11520       #   Rem to ensure Excel is set with same value.

global runInit          #   A switch so we can run some code on startup
runInit = True


def getComm():
    try:
        uart.init(baudrate=BAUD_Rate, bits=8, parity=None, stop=1)
        #sleep(1)                    #  can't quite decide if this helps marginally (with the success rate of the COM comm) or not.
                                     #  ... the way I read the buffer means these 1s add up though, so unless I can see a need its out for now.
        buf = bytearray(1)           #  Not an ideal method - read one char at a time... very slow.  First iteration only (built from POC code)
        
        if(uart.any()):
            uart.readinto(buf, 1)   #   reads 1 char from the USB / UART buffer into our bytearray buffer
        return(buf[0])

    except:
        uart.init(BAUD_Rate)        


def getImageDataFromUSB():          #   Called by main each cycle, this checks buffer and processes it 1 char at a time.
    global activeRow
    global bufStrFromUSB            #   Global cos we pass through this a single char at a time and add to this buffer
    
    intBuf = getComm()
        
    #   Rule: first char of a target comm mus be 'X' - ASCII = 88
    if(intBuf == 88):               #   initialise a new raw row record:
        activeRow = True            #   This switch means that this and the next 7 chars to be read will be added to the str buffer
        bufStrFromUSB = "X"         #   Not really necessary - we could dispense with this - its first iteration (POC) code.

    if(activeRow):      
        if(intBuf > 47 and intBuf < 58):                        # we are only interested in integers - we consume all other data.
            bufStrFromUSB = bufStrFromUSB + str(chr(intBuf))

    #   Rule: a valid image record row will have 8, no more, no less, chars.
    if (len(bufStrFromUSB) == 8):
        activeRow = False           # we have received the full row of data - no need to process more.
        processRawRowData(bufStrFromUSB)


def processRawRowData(rawRowStr):
    #global rawImageDataFrameIDs
    try:
        frameID = int(rawRowStr[1])
        rowID = int(rawRowStr[2])
        #rawImageDataFrameIDs[rowID] = frameID      #   hidden - introduces performance issues with animations.  Will fix in next version.
        rawImageData = str(rawRowStr[3:8])
        if(not(rowID  == 4)): 
            rawImageData = rawImageData  +":"       #   getting ':' added now (row separator) so we can make image str easily later on.
        rawImageStrData[rowID] = rawImageData
        checkAndFinaliseImage(frameID)
        return
    except:
        return


def checkAndFinaliseImage(frameID):
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


def checkImageIsReady():
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

    if(button_a.was_pressed()):
        display.show(Image((imageDataStore[0])))
        sleep(1000)

    if(button_b.was_pressed()):
        for i in range (0, 10):
            display.show(Image((imageDataStore[i])))
            sleep(500)