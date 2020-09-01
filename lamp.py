#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)
RELAIS_1_GPIO = 27
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
tijdAan = 7
tijdUit = 23

LampToestand="False"

while True :
  DateNow = datetime.now()
  uur = DateNow.hour

  if uur >= tijdAan and uur < tijdUit :  # lamp aan om tijdAan
      GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # aan
      if LampToestand != "Aan" :
       LampToestand = "Aan"
       f= open("/home/pi/logs/TriggerEvents.txt","a+")
       f.write(datetime.now().ctime() + "  Lamp  " +  LampToestand +  "\n")
       f.close()

  elif uur >= tijdUit or uur < tijdAan : # lamp uit om tijdUit
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

