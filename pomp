#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)

loop = "loop"
PompToestand="False"

while loop == "loop" :
  DateNow = datetime.now()
  uur = DateNow.hour
  minuut = DateNow.minute

  if uur == 8 and minuut <= 5 :  # pomp aan om 08, 5 minuten
      GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aan
      if PompToestand != "Aan" :
       PompToestand = "Aan"
       f= open("/home/pi/logs/TriggerEvents.txt","a+")
       f.write(datetime.now().ctime() + "  Pomp  " +  PompToestand +  "\n")
       f.close()

  elif uur == 16 and minuut <= 5 :  # pomp aan om 16, 5 minuten
      GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aan
      if PompToestand != "Aan" :
       PompToestand = "Aan"
       f= open("/home/pi/logs/TriggerEvents.txt","a+")
       f.write(datetime.now().ctime() + "  Pomp  " +  PompToestand +  "\n")
       f.close()
       time.sleep(300) #hier laat ik het script 5 minuten slapen. stel dat we d$
  elif uur == 0 and minuut <= 5 :  # pomp aan om 0, 5 minuten
      GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aan
      if PompToestand != "Aan" :
       PompToestand = "Aan"
       f= open("/home/pi/logs/TriggerEvents.txt","a+")
       f.write(datetime.now().ctime() + "  Pomp  " +  PompToestand +  "\n")
       f.close()
       time.sleep(300)

  else :
      GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # aan
      if PompToestand != "Uit" :
       PompToestand = "Uit"
       f= open("/home/pi/logs/TriggerEvents.txt","a+")
       f.write(datetime.now().ctime() + "  Pomp  " +  PompToestand +  "\n")
       f.close()
       time.sleep(300)

