#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

num_attemps = 20

while (num_attemps != 200):
  num_attemps += 1
  GPIO.setup(num_attemps,GPIO.OUT)
  GPIO.output(num_attemps,GPIO.HIGH)
  print num_attemps
  time.sleep(1)
  GPIO.output(num_attemps,GPIO.LOW)
  time.sleep(1)
