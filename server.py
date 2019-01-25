#!/usr/bin/env python3

# SETUP
#
# sudo pip3 install requests
#
# Create "config.py" with all the configurations:
#
# nano config.py 
#
# PASTE THIS:
# ------------------------------------------
# SERVER = '192.168.1.1:80'
#
# Username and Password must be inserted in CODE64 format, convert here: https://codebeautify.org/base64-encode
# USER = 'user'
# PASS = 'pass'
#
# IDX_INTERCOM = 'x'
# API_URL = 'http://'+SERVER+'/json.htm'
# ------------------------------------------
#
import config

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import requests
from threading import Thread

SERVER = config.SERVER
USER = config.USER
PASS = config.PASS

IDX_INTERCOM = config.IDX_INTERCOM
API_URL = config.API_URL

num_attemps = 0

def ring_intercom():
  global SERVER
  global USER
  global PASS
  global IDX_INTERCOM
  global API_URL
  global num_attemps

  postdata = {'username':USER, 'password':PASS, 'type':'devices', 'rid':IDX_INTERCOM}
  resp = requests.get(url=API_URL, params=postdata)
  data = resp.json()

  result = data['result'][0]['Status']

  if (result == 'Off'):
        postdata = {'username':USER, 'password':PASS, 'type':'command', 'param':'switchlight', 'idx':IDX_INTERCOM, 'switchcmd':'On'}
        resp = requests.get(url=API_URL, params=postdata)
        data = resp.json()
        if data['status'] == 'OK':
                num_attemps = 0
        else:
                num_attemps += 1
                if num_attemps < 5:
                  time.sleep(1)
                  ring_intercom()

######## CHECK VOLTAGE SPIKES TO RECOGNIZE THE RING ######## 
def check_intercom():
  ### ADC PART ###
  # Create the I2C bus
  i2c = busio.I2C(board.SCL, board.SDA)
  # Create the ADC object using the I2C bus
  ads = ADS.ADS1115(i2c)
  # Create single-ended input on channel 0
  chan = AnalogIn(ads, ADS.P0)

  while True:
    voltaggio = float(chan.voltage)
    if voltaggio > 1:
      ring_intercom()

if __name__ == '__main__':
  Thread(target=check_intercom).start()