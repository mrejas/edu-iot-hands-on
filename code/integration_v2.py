#!/usr/bin/python

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import json

topic_write="set/tuc/led1"
topic_read="obj/tuc/led1"

led = 16

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led,GPIO.OUT)

client=mqtt.Client()
client.connect("localhost")

def on_message(client, userdata, message):

    payload = json.loads(message.payload)

    if message.topic == topic_write:
        if payload["value"] == 0:
            print("Turning led off")
            GPIO.output(led,0)
            client.publish(topic_read, '{"value":0, "timestamp":' + str(time.time()) + '}')
        else:
            print("Turning led on")
            GPIO.output(led,1)
            client.publish(topic_read, '{"value":1, "timestamp":' + str(time.time()) + '}')
    else:
        print("Ignoring " + message.topic)

print("Subscribing to topic " + topic_write)
client.subscribe(topic_write)
client.on_message=on_message

client.loop_forever()
