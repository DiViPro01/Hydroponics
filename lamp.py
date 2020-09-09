#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)
RELAIS_1_GPIO = 27
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
HourOn = 7
HourOff = 23

LampStatus="False"

while True :
  DateNow = datetime.now()
  hour = DateNow.hour

  if hour >= HourOn and hour < HourOff :  # lamp aan om tijdAan
      GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aan
      if LampStatus != "On" :
       LampStatus = "On"
       f= open("/home/pi/logs/TriggerEvents.txt","a+")
       f.write(datetime.now().ctime() + "  Lamp  " +  LampStatus +  "\n")
       f.close()

  elif hour >= HourOff or hour < HourOn : # lamp uit om tijdUit
      GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # uit
      if LampStatus != "Off" :
        LampToestand = "Off"
        f= open("/home/pi/logs/TriggerEvents.txt","a+")
        f.write(datetime.now().ctime() + "  Lamp  " + LampStatus +  "\n")
        f.close()

  else :
        f= open("/home/pi/logs/TriggerEvents.txt","a+")
        f.write(datetime.now().ctime() + "  Error in lamp script " +  "\n")
        f.close()


  time.sleep(60)

