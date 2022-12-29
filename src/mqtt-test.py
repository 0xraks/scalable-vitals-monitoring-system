import paho.mqtt.client as mqtt
import json
import random

MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "/raka"

idval=10032

mqttc = mqtt.Client()
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
sendstr={"id": idval ,"heartrate":random.randint(65,90),"spo2":random.randint(80,100),"temp":random.randint(35,42)}
MQTT_MSG=json.dumps(sendstr);
mqttc.publish(MQTT_TOPIC, MQTT_MSG)
