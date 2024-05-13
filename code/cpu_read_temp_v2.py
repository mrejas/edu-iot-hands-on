#!/usr/bin/python
import paho.mqtt.client as mqtt
import time
import json

topic_read="obj/rpi/cpu_temp"
topic_trigger="cmd/rpi/cpu_temp"

client = mqtt.Client()
client.connect("localhost")

def get_cpu_temp():
    fd = open("/sys/class/thermal/thermal_zone0/temp", "r")
    millidegs = fd.readline()
    fd.close()
    temp = int(millidegs) / 1000.0
    return temp


def on_message(client, userdata, message):
    client.publish(topic_read, '{"value":' + str(get_cpu_temp()) + ', "timestamp":' + str(time.time()) + '}')


print("Subscribing to topic " + topic_trigger)
client.subscribe(topic_trigger)
client.on_message=on_message

client.loop_forever()
