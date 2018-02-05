from microbit import *
#from sys import print_exception

# We'll set up a simple String buffer that can carry 10 images (for previewing animations).
global imageDataStore 
imageDataStore = ["", "", "", "", "", "", "", "", "", ""]

global imageDataReady       #   This switch indicates when all data for an image (5 rows) has been loaded.
imageDataReady = False

# We will read each row into an array as they are received:
global rawImageStrData
rawImageStrData = ["", "", "", "", ""]

# we use a switch - when an active row is detected (i.e. metadatas from serial comms indicates beginning of image data) we turn it True and read into the array.
global activeRow
activeRow = False

global currentFrame     #   To support animation preview we will allow up to 10 frames to be sent over.
currentFrame = 0

global bufStrFromUSB
bufStrFromUSB = ""

#uart.init(9600,8,1)

#readBuf = bytearray(2)

def getComm():
    try:
        uart.init(baudrate=9600, bits=8, parity=None, stop=1)
        sleep(1)
        buf = bytearray(1)
        
        if(uart.any()):
            uart.readinto(buf, 1)

        return(buf[0])

    except Exception as exc:
        uart.init(9600)
        #print_exception(exc)

def getImageDataFromUSB():
    global activeRow
    global bufStrFromUSB
    
    intBuf = getComm()
        
        
    #   Rule: first char of a target comm mus be 'X' - ASCII = 88
    if(intBuf == 88):       # initialise a new raw row record:
        activeRow = True
        bufStrFromUSB = ""
        
    #   Rule: a valid image record row will have 8, no more, no less, chars.
    if (len(bufStrFromUSB) == 8):
        activeRow = False           # we have received the full row of data - no need to process more.
        processRawRowData(bufStrFromUSB)
   
    if(activeRow):      # Below we are only interested in numerals and upper case chars - consume all other info below.    
        if(     (intBuf > 47 and intBuf < 58) or  (intBuf > 64 and intBuf < 91) ):
            bufStrFromUSB = bufStrFromUSB + str(chr(intBuf))
            #display.show(str(len(bufStrFromUSB)))

def processRawRowData(rawRowStr):
    frameID = int(rawRowStr[1])
    rowID = int(rawRowStr[2])
    rawImageData = str(rawRowStr[3:8])
    if(not(rowID  == 4)): rawImageData = rawImageData  +":"
    
    rawImageStrData[rowID] = rawImageData
    
    checkAndFinaliseImage(frameID)


def checkAndFinaliseImage(frameID):
    global imageDataReady
    global rawImageStrData
    # we will check if all data for the current frame has been received - if so we'll add it to the imageID frame:
    imageIsReady = True
    
    for i in range(0, 5):
        if(len(rawImageStrData[i]) < 5): imageIsReady = False

    if(imageIsReady):
        allImageData = ""
        for i in range(0, 5):
            allImageData  = allImageData  + rawImageStrData[i]
        imageDataStore[frameID] = allImageData
        display.show(Image(imageDataStore[frameID]))
        imageDataReady = True
        
        #for i in range(0, 4):
        #    rawImageStrData[i] = ""     #   reset the buffer to ensure we only process a complete image
             

while True:
    getImageDataFromUSB()

    if(button_a.was_pressed()):
        display.show(Image((imageDataStore[0])))
        sleep(1000)
        #uart.write("")

    if(button_b.was_pressed()):
        for i in range (0, 10):
            display.show(Image((imageDataStore[i])))
            sleep(500)