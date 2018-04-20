### --- Programmi konfi osa

logFile = 'testlog.txt'

### --- Input-Output seadme konf
# palju on I2C sisendseadmeid.
seadmeid = 1

###### --- MQTT konfiguratsiooni osa --- ######

MQTT_HOST = "192.168.1.99"
MQTT_seade = "klent1"
MQTT_port = 1883
MQTT_user = "openhabian"
MQTT_password = "m4q22tt65"
MQTT_sub_topic = "home/data"                       # receive messages on this topic
MQTT_pub_topic = "home/instructions"               # send messages to this topic
MQTT_KEEPALIVE_INTERVAL = 60
