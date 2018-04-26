#!/usr/bin/python

### -- KONFI OSA --- ###
logFile = 'testlog.txt'
statusMap = [*OFF', 'ON']

import datetime
import time
#import config
#import mqtt

from mcp23017 import mcp23017, pin

pin_count = 8
seade = 1
# GPIOA = 0, GPIOB = 1
MCP_port = ['gpioa', 'gpiob']
# Seade 0x20 =0, 0x21=1, 0x22=2 jne
MCP_seade = ['0x20', '0x21']

#arming_status = false
inpin = ([],[])

# Algseadista sisendite vaatus = 1 (signaal peal)
inpin = [[1 for j in range(2)] for i in range(pin_count)]


def read_Input(s_addr,s_port):
    seade = MCP_seade[s_addr]
    port = MCP_port[s_port]
    mpin = 0
    mymcp = mcp23017()
#    print (seade, port)
    seis = inpin[mpin][s_port]
    while (mpin < pin_count):
#        print ("Sisend:", port, "-", mpin, "value-", inpin[mpin][s_port])
        mypin = pin(mymcp, str(port), mpin)
        seis = mypin.value()
        aeg = str(currentDT.strftime('%Y/%m/%d %H:%M:%S'))
        if seis != inpin[mpin][s_port]:
           print (aeg, "ALARM: Sisend:", port, "-", mpin, "value -", inpin[mpin][s_port], "muudetud =", seis)
# Kirjuta alarm logisse
           f = open(logFile,'a')
           f.write(aeg + ': ALARM! Sisend: ' + str(port) + ' pin-' + str(mpin + 1) + ' seis = ' + str(seis) + '\n')
           f.close()

#                MQTT_sens
           client = mqtt.Client()
           client.username_pw_set(MQTT_user, password=MQTT_password)
           client.on_connect = on_connect
           client.connect(MQTT_HOST, MQTT_port, MQTT_KEEPALIVE_INTERVAL)
           client.on_log = on_log
           client.publish_mqtt = publish_mqtt(MQTT_pub_topic + MQTT_seade + str(seade) + '_' + str(port) + '_' + str(mpin + 1), statusMap[seis])
           client.disconnect()
# Salvesta viimane sisendi väärtus
           inpin[mpin][s_port] = seis

#        else:
#          print ("Sisend:", port, "-", mpin, "value", inpin[mpin][s_port], "muutmata")
        mpin = mpin + 1


### ----- PROGRAMM --- ####
def main():
#Kļæ½vita programm
# Loo mqtt yhendus
# Loe MQTT kasud serverilt, tee tegevus
# Loe sisendid - read_Input(seade[0-0x20,1-0x21],sisendite_port[0-gpioa,1-gpiob])
    read_Input(0,0)
    read_Input(0,1)
#   read_Input(1,0)
#   read_Input(1,1)

if __name__ == "__main__":
#    while True:
        main()
#    sleep(1)