import paho.mqtt.client as mqtt
import json
# Define Variables
MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "/raka"

# Parameter  values
idval=10032
heartrate=72
spo2=98
temp=38

sendstr={"id": idval ,"heartrate":heartrate,"spo2":spo2,"temp": temp}
MQTT_MSG=json.dumps(sendstr);
mqttc = mqtt.Client()
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
mqttc.publish(MQTT_TOPIC, MQTT_MSG)
