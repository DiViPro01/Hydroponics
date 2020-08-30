#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)
RELAIS_1_GPIO = 18
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)

flag = "False"
while flag == "False":
  DateNow = datetime.now()
  uur = DateNow.hour
  if uur == 15 :  # lamp aan om 07 smorgens
      GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
  elif uur == 16 : # lamp uit om 01 smorgens
      GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # of
  else :
          print("doe niets")

