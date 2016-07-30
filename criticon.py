#coding:utf-8
#!/usr/bin/python

## taken from https://gist.github.com/loleg/5b581d774fc8500325f7
import random
import time
import sys
import json
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import zbar
import festival
from PIL import Image

# Debug mode
DEBUG = False
if len(sys.argv) > 1:
    DEBUG = sys.argv[-1] == '-d'

# Configuration options

if not DEBUG:
    RESOLUTION = (640, 480)
else:
    RESOLUTION = (480, 270)

json_file = open("data/db.json")

db = json.load(json_file)

# Initialise Raspberry Pi camera
camera = PiCamera()
camera.resolution = RESOLUTION
#camera.framerate = 10
#camera.vflip = True
#camera.hflip = True
#camera.color_effects = (128, 128)
# set up stream buffer
rawCapture = PiRGBArray(camera, size=RESOLUTION)
# allow camera to warm up
time.sleep(0.1)
print "PiCamera ready"

#sele
festival.execCommand("(voice_el_diphone)")

# Initialise OpenCV window
if DEBUG:
    #cv2.namedWindow("#iothack15", cv2.WND_PROP_FULLSCREEN)
    #cv2.setWindowProperty("#iothack15", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.namedWindow("#criticon")


print "OpenCV version: %s" % (cv2.__version__)
print "Press q to exit ..."

scanner = zbar.ImageScanner()
scanner.parse_config('enable')

# Capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # as raw NumPy array
    output = frame.array.copy()

    # raw detection code
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY, dstCn=0)
    pil = Image.fromarray(gray)
    width, height = pil.size
    raw = pil.tobytes()

    # create a reader
    image = zbar.Image(width, height, 'Y800', raw)
    scanner.scan(image)

    # extract results
    for symbol in image:
        # do something useful with results
        streeng = "decoded " + str(symbol.type) + " symbol " + str(symbol.data)
        print streeng
        tags = db['codes'][str(symbol.data)]
        text = random.choice(db[tags[0]]) + random.choice(db[tags[1]])
        print(text)
        festival.sayText(text)


    # show the frame
    if DEBUG:
        cv2.imshow("#criticon", output)

    # clear stream for next frame
    rawCapture.truncate(0)

    # Wait for the magic key
    keypress = cv2.waitKey(1) & 0xFF
    if keypress == ord('q'):
        break

# When everything is done, release the capture
camera.close()
if DEBUG:
    cv2.destroyAllWindows()
