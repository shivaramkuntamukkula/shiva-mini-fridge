import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)


for i in range(2):
    client.publish('mini', payload="START RASPBERRY PI MINIBAR", qos=0, retain=False)
    time.sleep(1)


#time.sleep(1)

#client.loop_forever()
