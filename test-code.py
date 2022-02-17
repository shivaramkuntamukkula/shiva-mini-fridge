



# GUI Python3 example on Raspberry Pi to handle notification from
# ESP32 BLE_notify example.
# To install bluepy for Python3:
# $ sudo pip3 install bluepy

from paho.mqtt import client as mqtt_client

from bluepy import btle
import time
import os 
import random


broker = 'broker.emqx.io'
port = 1883
topic = "mini"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'meini'
password = '1234'
#------------MQTT-----------------------------------------------------

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("MQTT.......")
            #print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
   # print("1")
    client.username_pw_set(username, password)
    #print("2")    
    client.on_connect = on_connect
    #print("3")
    client.connect(broker, port)
    #print("1")
    return client
#client = connect_mqtt()

def subscribe(client: mqtt_client):
   # print("a")
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if (msg.payload.decode())=="START":
            print("sending RESET command to ESP32")
            g= bytes('start', 'utf-8')
            p.writeCharacteristic(handle, g)
        #time.sleep(0.5)
    client.subscribe(topic)
    #print("b")
    client.on_message = on_message
    #print("c")
def run():
    client = connect_mqtt()
    print("p")
    subscribe(client)
    print("q")
    print("subscribed")
    print("r")
    client.loop_forever()
    print("s")

#-------------------------------------------------------------------------------



class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        # ... initialise here
     

  
    def writeCharacteristic(handle,val,withResponse):
        print(withResponse)



    def handleNotification(self, cHandle, data):

       		# ... perhaps check cHandle

		# # ... process 'data'  
        if(cHandle==0x002a):

            highbyte7=(data[1])
            lowbit7=(data[0])
            word7=(highbyte7<<8)|lowbit7
            print("the weight of J7  : " +str(word7))
            xx=str(word7)
           


 #-------------------------------------------------------------
        elif(cHandle==0x002d):


            highbyte=(data[0])
            lowbit=(data[1])
         #  print(data[0])
         # print(data[1])

            word=(highbyte<<8)|lowbit
            print("the weight of J5  : " +str(word))
            print("        ")
            
            #os.system('clear')

## Initialisation  -------

#address = "08:3A:F2:6E:29:CA"
address = "A4:CF:12:6B:60:1E"

service_uuid = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
char_uuid = "beb5483e-36e1-4688-b7f5-ea07361b26a8"
char_uuid_02 = "dd2ca829-8b7e-4a1a-936e-3409f2c85855"

#try:
#    p = btle.Peripheral(address)
#    p.setDelegate(MyDelegate())
#    svc = p.getServiceByUUID(service_uuid)
#    ch = svc.getCharacteristics(char_uuid)[0]
#    ch_02 = svc.getCharacteristics(char_uuid_02)[0]
#    ch_data = p.readCharacteristic(ch.valHandle + 1)
#    ch_data_02 = p.readCharacteristic(ch_02.valHandle + 1)
#except:
#    print("not connected")  


# Setup to turn notifications on, e.g.
#svc = p.getServiceByUUID(service_uuid)

#ch = svc.getCharacteristics(char_uuid)[0]
#ch_02 = svc.getCharacteristics(char_uuid_02)[0]
"""
setup_data for bluepy noification-
"""
#setup_data = b"\x01\x00"
 #ch.write(setup_data)

#p.writeCharacteristic(ch.valHandle + 1, setup_data)
#p.writeCharacteristic(ch_02.valHandle + 1, setup_data)

#p.writeCharacteristic(0x0030,0x03, False)

#ch_data = p.readCharacteristic(ch.valHandle + 1)
#ch_data_02 = p.readCharacteristic(ch_02.valHandle + 1)

#print(type(ch_data))
#print(ch_data)
handle=0x0030     #handle of the write characteristics


enb=1
while True:
    
    if enb==1:
        try:
           # print("Initialing connection with ESP32............")
            p = btle.Peripheral(address)
            p.setDelegate(MyDelegate())
            enb=0
            print("Connected to ESP32 of the Minibar-Livello "+str(enb))
        except:
            print("Not connected yet")  
            enb=1
            time.sleep(2)
    elif enb==0:
        try:
            svc = p.getServiceByUUID(service_uuid)
            ch = svc.getCharacteristics(char_uuid)[0]
            ch_02 = svc.getCharacteristics(char_uuid_02)[0]
            setup_data = b"\x01\x00"
            p.writeCharacteristic(ch.valHandle + 1, setup_data)
            p.writeCharacteristic(ch_02.valHandle + 1, setup_data)
            ch_data = p.readCharacteristic(ch.valHandle + 1)
            ch_data_02 = p.readCharacteristic(ch_02.valHandle + 1)
            g= bytes('CHECK', 'utf-8')
            p.writeCharacteristic(handle, g)
            print("WRITE TO ESP CODE LINE PASSED WITHOUT ERROR")
            #if p.waitForNotifications(1.0):
    #        time.sleep(1)
            print("inside the try with CVS   "+ str(enb))
         #   client = connect_mqtt() #    continue
            
            enb=2
            
            
        except:
            print("something went wrong~!")
            enb=1

 #   print("loop started ")
   #= bytes('start', 'utf-8')
 #   p.writeCharacteristic(handle, g)
    #writeCharacteristic(handle, val, withResponse=True)

    if enb==2:   

        client = connect_mqtt()
         #print("p")
        subscribe(client)
 #       print("q")
        print("subscribing....")
  #      print("r")
        client.loop_start()
   #     print("s")
        time.sleep(0.5)         
#        while True:
    #    print("enable..2 passed")
       # while True:   
        #print("waiting for notification"+str(enb))
            #client = connect_mqtt()           
            #subscribe(client)
        client.loop_stop()       
            #time.sleep(1)
        if p.waitForNotifications(1):

            time.sleep(0.2)
         #   g= bytes('START/STOP CMD', 'utf-8')
          #  p.writeCharacteristic(handle, g)
           # print("Sending CMD to ESP32") 
            continue
 #   if p.waitForNotifications(1.0):

    # handleNotification() was called
  #      continue
    #    print("Waiting...")
    # Perhaps do something else here

