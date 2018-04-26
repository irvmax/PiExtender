### --- Programmi konfi osa

logFile = 'testlog.txt'

### --- Input-Output seadme konf
# palju on I2C sisendseadmeid.
seadmeid = 1

###### --- MQTT konfiguratsiooni osa --- ######

MQTT_HOST = "IP_XXX.XXX.XXX.XXX"
MQTT_seade = "SEADE"
MQTT_port = 1883
MQTT_user = "MQTT-USER"
MQTT_password = "MQTT-PASS"
MQTT_sub_topic = "home/data"                       # receive messages on this topic
MQTT_pub_topic = "home/instructions"               # send messages to this topic
MQTT_KEEPALIVE_INTERVAL = 60
