#!/usr/bin/python

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

photores = 24
LED = 25
topic_read = "obj/tuc/photo"

client = mqtt.Client()
client.connect("localhost")

GPIO.setup(photores,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)

last_state=-1

while True:
    photores_state = GPIO.input(photores)
    if photores_state == 0 and last_state != 0:
        GPIO.output(LED,GPIO.HIGH)
        client.publish(topic_read, '{"value":' + '0' + ', "timestamp":' + str(time.time()) + '}')
        last_state = 0
    elif photores_state == 1 and last_state != 1:
        GPIO.output(LED,GPIO.LOW)
        client.publish(topic_read, '{"value":' + '1' + ', "timestamp":' + str(time.time()) + '}')
        last_state = 1
    time.sleep(0.2)
