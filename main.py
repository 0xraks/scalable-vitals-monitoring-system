from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
from pyzbar import pyzbar
from smbus2 import SMBus
from mlx90614 import MLX90614
import max30100

mx30 = max30100.MAX30100()
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)

def get_mlxtemp():
    #print ("Ambient Temperature :", sensor.get_ambient())
    return int(sensor.get_object_1())
def get_maxvalues():
    counter=10
    mx30.reinit()
	mx30.set_mode(max30100.MODE_SPO2)
    mx30.read_sensor()
	hrval=mx30.ir
	spOval=mx30.red
    pubval1=max30100.convertval(mx30.red)
	pubval2=max30100.convertit(mx30.ir)
    print(pubval1)
    print(pubval2)



# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	frame = frame.array
		# find the barcodes in the frame and decode each of the barcodes
	barcodes = pyzbar.decode(frame)
	if (len(barcodes)>0):
                print (barcodes[0].data.decode("utf-8"))
                print(get_mlxtemp())
                # show the frame
	#cv2.imshow("Vitals Monitoring System", frame)
	key = cv2.waitKey(1) & 0xFF
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
