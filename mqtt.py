from paho.mqtt.client import Client

client = Client(client_id="citofono_1")


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload.decode("utf-8")))


client.on_message = on_message
client.username_pw_set(username="", password="")
client.connect("10.50.0.55")
client.subscribe("citofono", qos=0)

client.loop_forever()
