from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
from pyzbar import pyzbar
from smbus2 import SMBus
from mlx90614 import MLX90614
import max30100
import RPi.GPIO as GPIO

mx30 = max30100.MAX30100()
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)

def get_mlxtemp():
	#print ("Ambient Temperature :", sensor.get_ambient())
	return int(sensor.get_object_1())

def average(lst):
	return sum(lst) / len(lst)

def get_maxvalues():
	counter=20
	hr_vals=[]
	sp_vals=[]
	while(counter !=0 ):
		mx30.reinit()
		mx30.set_mode(max30100.MODE_SPO2)
		mx30.read_sensor()
		hrval=mx30.ir
		spOval=mx30.red
		pubval1=max30100.convertval(mx30.red)
		pubval2=max30100.convertit(mx30.ir)
		if ((pubval1 > 30) and (pubval2 > 30)):
			sp_vals.append(pubval1)
			hr_vals.append(pubval2)
		time.sleep(0.25)
		if (len(sp_vals)!=0):
			counter=counter-1
	mx30.reset()
	print(average(hr_vals))
	print(average(sp_vals))

def gpio_buzzer(buzzer):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(buzzer,GPIO.OUT)
	GPIO.output(buzzer,GPIO.HIGH)
	time.sleep(0.05)
	GPIO.output(buzzer,GPIO.LOW)
	time.sleep(0.05)
	GPIO.output(buzzer,GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(buzzer,GPIO.LOW)
	

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	frame = frame.array
	barcodes = pyzbar.decode(frame)
	if (len(barcodes)>0):
                print (barcodes[0].data.decode("utf-8"))
                gpio_buzzer(14)
                get_maxvalues()
                print(get_mlxtemp()+5)
                
	#cv2.imshow("Vitals Monitoring System", frame)
	key = cv2.waitKey(1) & 0xFF
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

