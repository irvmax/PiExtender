#######--- Konfiguratsiooni osa ---######

MQTT_HOST = "192.168.1.99"
MQTT_seade = "klent1"
MQTT_port = 1883
MQTT_user = "openhabian"
MQTT_password = "m4q22tt65"
MQTT_sub_topic = "home/data"    # receive messages on this topic
MQTT_pub_topic = "home/sensor/"               # send messages to this topic
MQTT_KEEPALIVE_INTERVAL = 60

#######--- Programmi osa ---######

import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

Connected = False             # global variable for the state of the connection
############### MQTT section ##################

# when connecting to mqtt do this;

def on_connect(client, userdata, flags, rc):
	if rc ==0:
		print("Connected with result code "+str(rc))
		global Connected
		Connected = True
		client.subscribe(MQTT_sub_topic)
	else:
		print("Connection failed")

def on_log(client, userdata, level, buf):
    print("log: ",buf)
# when receiving a mqtt message do this;

def on_message(client, userdata, msg):
    message = str(msg.payload)
    print(msg.topic+" "+message)
    publish_mqtt('got your message'+str(msg.payload))

# to send a message

def publish_mqtt(sensor_topic, sensor_data):
    mqttc = mqtt.Client(MQTT_seade)
    mqttc.connect(MQTT_HOST, MQTT_port)
    mqttc.publish(sensor_topic, sensor_data)
#    client.disconnect()
    #mqttc.loop(2) //timeout = 2s

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))


client = mqtt.Client()
client.username_pw_set(MQTT_user, password=MQTT_password)
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_HOST, MQTT_port, MQTT_KEEPALIVE_INTERVAL)
client.on_log=on_log
#client.publish_mqtt = publish_mqtt('hello')
client.loop_forever()
