#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

photores = 24
LED = 25

GPIO.setup(photores,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)

while True:
    photores_state = GPIO.input(photores)
    print(photores_state)
    if photores_state == 0:
        GPIO.output(LED,GPIO.HIGH)
    else:
        GPIO.output(LED,GPIO.LOW)
    sleep(0.2)
