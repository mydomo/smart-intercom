#!/usr/bin/env python3

import config
from paho.mqtt.client import Client
import RPi.GPIO as GPIO
import time

MQTT_USER = config.MQTT_USER
MQTT_PASS = config.MQTT_PASS

client = Client(client_id="citofono_1")

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)

def on_message(client, userdata, msg):
    if str(msg.payload.decode("utf-8")) == "open":
        GPIO.output(26,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(26,GPIO.LOW)

client.on_message = on_message
client.username_pw_set(username= MQTT_USER, password= MQTT_PASS)
client.connect("10.50.0.55")
client.subscribe("citofono", qos=0)

client.loop_forever()
