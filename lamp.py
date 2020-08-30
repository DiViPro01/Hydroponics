#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)
RELAIS_1_GPIO = 18
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)

f= open("TriggerEvents.txt","a+")
flag = "False"
LampToestand="False"

while flag == "False":
  DateNow = datetime.now()
  uur = DateNow.hour
  if uur >= 9 and uur <= 24 :  # lamp aan om 09
      GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
      if LampToestand != "Aan" :
       LampToestand = "Aan"
       f.write(datetime.now().ctime() + "  Lamp  " +  LampToestand +  "\n")
  elif uur >= 01 and uur <= 8 : # lamp uit om 01
      GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # uit
      if LampToestand != "Uit" :
        LampToestand = "Uit"
        f.write(datetime.now().ctime() + "  Lamp  " + LampToestand +  "\n")
  else :
          print("doe niets")