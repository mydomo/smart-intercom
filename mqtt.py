import config
from paho.mqtt.client import Client

MQTT_USER = config.MQTT_USER
MQTT_PASS = config.MQTT_PASS
client = Client(client_id="citofono_1")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload.decode("utf-8")))


client.on_message = on_message
client.username_pw_set(username= MQTT_USER, password= MQTT_PASS)
client.connect("10.50.0.55")
client.subscribe("citofono", qos=0)

client.loop_forever()
