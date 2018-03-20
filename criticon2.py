#coding:latin-1
#!/usr/bin/python

## taken from https://gist.github.com/loleg/5b581d774fc8500325f7
import os
import sys
import time
import random
import json
#from picamera.array import PiRGBArray
#from picamera import PiCamera
import cv2
import zbarlight as zbar
import festival
from PIL import Image
import RPi.GPIO as gpio


# Debug mode
DEBUG = False
if len(sys.argv) > 1:
    DEBUG = sys.argv[-1] == '-d'

# Configuration options

if not DEBUG:
    RESOLUTION = (640, 480)
else:
    RESOLUTION = (480, 270)

gpio.setmode(gpio.BOARD)
gpio.setup(8, gpio.OUT)


# Initialise Raspberry Pi camera
#camera = PiCamera()
#camera.resolution = RESOLUTION

#camera.framerate = 10
#camera.vflip = True
#camera.hflip = True
#camera.color_effects = (128, 128)
# set up stream buffer

#rawCapture = PiRGBArray(camera, size=RESOLUTION)

# allow camera to warm up

cap = cv2.VideoCapture(0)

print("Camera ready")

#turn the led on
gpio.output(8, gpio.HIGH)

#seleccionar voz en espaõl
festival.execCommand("(voice_JuntaDeAndalucia_es_sf_diphone)")
# Initialise OpenCV window
if DEBUG:
    cv2.namedWindow("#criticon")


print("OpenCV version: %s" % cv2.__version__)
print("Press q to exit ...")

wait = 4
count = wait;

os.system( "echo criticó ha despertado, buscando código de barras. | iconv -f utf-8 -t iso-8859-1 | festival --tts")


while(True):
    # Capture frame-by-frame
    cap.grab()
    ret, frame = cap.retrieve()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY, dstCn=0)
    pilimg = Image.fromarray(gray)
    width, height = pilimg.size

    # create a reader
    codes = zbar.scan_codes('code128', pilimg)
    print(codes)
    if codes:
        for symbol in codes:
            if count < wait:
                count = count + 1
            else:
                count = 0;
                data = symbol.decode('utf-8')
                streeng = "decoded symbol: " + data
                print(streeng)
                try:
                    tags = db['codes'][data]
                    _text = random.choice(db[tags[0]]) + random.choice(db[tags[1]])
                    #text = _text.encode('utf-8')
                    print(_text)
                    cmd = "echo " + _text + " | iconv -f utf-8 -t iso-8859-1 | festival --tts"
                    os.system(cmd)
                    #festival.sayText(text.encode('latin-1'))

                except KeyError:
                    os.system( "echo criticón no reconoce el lenguaje de esta obra. | iconv -f utf-8 -t iso-8859-1 | festival --tts")
            streeng = "decoded symbol: " + str(symbol)
            print(streeng)
            try:
                tags = db['codes'][str(symbol)]

                _text = random.choice(db[tags[0]]) + random.choice(db[tags[1]])
                text = _text.encode('utf-8')
                print(text)
                cmd = "echo " + text + " | iconv -f utf-8 -t iso-8859-1 | festival --tts"
                os.system(cmd)
                #festival.sayText(text.encode('latin-1'))

            except KeyError:
                os.system( "echo criticón no reconoce el lenguaje de esta obra. | iconv -f utf-8 -t iso-8859-1 | festival --tts")


    # show the frame
    if DEBUG:
        cv2.imshow("#criticon", frame)

    # clear stream for next frame

    # Wait for the magic key
    keypress = cv2.waitKey(1) & 0xFF
    if keypress == ord('q'):
        break

#turn off led
gpio.output(8, gpio.LOW)

# When everything is done, release the capture
camera.close()
if DEBUG:
    cv2.destroyAllWindows()
