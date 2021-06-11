import os
import sys
import time
import max30100
import paho.mqtt.client as mqtt



def main():
	try:
		mx30 = max30100.MAX30100()
		client = mqtt.Client()
		client.connect("192.168.0.42",1883,60) 
		# mx30.set_mode(max30100.MODE_SPO2)
		# mx30.reset()
		# time.sleep(1)
		# mx30.startup()
		# time.sleep(1)
		while (True):
			# mx30.set_mode(max30100.MODE_HR)
			# mx30.read_sensor()
			# # The latest values are now available via .ir and .red
			# print("HeartRate sensor .ir: {} and .red: {}".format(mx30.ir, mx30.red))

			# time.sleep(2)
			# mx30 = max30100.MAX30100()
			mx30.reinit()
			mx30.set_mode(max30100.MODE_SPO2)
			# time.sleep(1)

			mx30.read_sensor()
			hrval=mx30.ir
			spOval=mx30.red
			pubval1=max30100.convertval(mx30.red)
			pubval2=max30100.convertit(mx30.ir)
			
			#print(convertit(hrval))
			client.publish("/k1/sp02",pubval1)
			print("Published SPO2")
			client.publish("/k1/hr",pubval2)
			print("Published HEART-RATE")
			
			#print(mx30.get_temperature())
			#temp = mx30.get_temperature()
			#print("Temperature {}\n".format(temp))
			mx30.reset()
			time.sleep(1)
		mx30.reset()
		# mx30.shutdown()


	except Exception as e:
		print("Max30100 got exception {}".format(e))


if __name__ == "__main__":
  main()
  
