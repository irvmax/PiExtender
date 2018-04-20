# !/usr/bin/python
import datetime
from mcp23017 import mcp23017, pin
from time import sleep

sisend = 0
mymcp = mcp23017()
mypin = pin(mymcp, "gpioa", sisend)
while True:
    currentDT = datedime.datedime.now()
    seis = mypin.value()
        if seis == 0:
            print(currentDT.strftime("%Y-%m-%d %H:%M:%S"), "Alarm sisendis ->", sisend, seis)
        if sisend < 7
            sisens = sisend + 1
        else:
            sisend = 0

sleep(1)
