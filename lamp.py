#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)
RELAIS_1_GPIO = 27
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)

loop = "loop"
LampToestand="False"

while loop == "loop" :
  DateNow = datetime.now()
  uur = DateNow.hour

  if uur >= 8 and uur <= 24 :  # lamp aan om 08
      GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aan
      if LampToestand != "Aan" :
       LampToestand = "Aan"
       f= open("/home/pi/logs/TriggerEvents.txt","a+")
       f.write(datetime.now().ctime() + "  Lamp  " +  LampToestand +  "\n")
       f.close()

  elif uur >= 1 and uur <= 7 : # lamp uit om 01
      GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # uit
      if LampToestand != "Uit" :
        LampToestand = "Uit"
        f= open("/home/pi/logs/TriggerEvents.txt","a+")
        f.write(datetime.now().ctime() + "  Lamp  " + LampToestand +  "\n")
        f.close()

  else :
        f= open("/home/pi/logs/TriggerEvents.txt","a+")
        f.write(datetime.now().ctime() + "  FOUT IN SCRIPT LAMP " +  "\n")
        f.close()


  time.sleep(1800)
