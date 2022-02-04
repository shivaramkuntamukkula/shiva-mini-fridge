# GUI Python3 example on Raspberry Pi to handle notification from
# ESP32 BLE_notify example.
# To install bluepy for Python3:
# $ sudo pip3 install bluepy

from bluepy import btle
import matplotlib.pyplot as plt
import time
from os import system
"""value = [0]*30

plt.ylim([0, 256])
plt.plot(value)
plt.draw()
plt.pause(0.01)
"""
class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        # ... initialise here
    def handleNotification(self, cHandle, data):
		# ... perhaps check cHandle
		# ... process 'data'  
        #print(data[2])
        #print(data[3])

        highbyte7=(data[1])
        lowbit7=(data[0])
       #w7 = int(str(highbyte7) + str(lowbit7))
        #print(w7)
        word7=(highbyte7<<8)|lowbit7
        print("the weight of J7  : " +str(word7))
  #-------------------------------------------------------------
        print(type(data[3]))
       # print(dir(data[1]))
        highbyte=(data[1])
        lowbit=(data[0])
       
        print(data[0])
        print(data[1])
        #print(data[2])
        #print(data[3])
        

        w = int(str(highbyte) + str(lowbit))
       # print(w)
        word=(highbyte<<8)|lowbit
        #print("the weight of J5  : " +str(word))
        # full=(data[0])+(data[1])
        #print(full)
        #print(type(full))
  #i=1
        #for pin in data:
         #   print("\nThe weight reading "+ str(i) +" is  :  "+ str(int(pin)) + "grams\n" )
          #  print("...................")
           # i=i+1
  #      value.pop(0)
   #     value.append(data[0])
    #    plt.clf()
     #   plt.ylim([0, 256])
      #  plt.plot(value)
       # plt.draw()
        #plt.pause(0.01)
   
# Initialisation  -------
address = "A4:CF:12:6B:60:1E"
service_uuid = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
char_uuid = "beb5483e-36e1-4688-b7f5-ea07361b26a8"
#char2_uuid = "76e69b2f-229d-4c5d-8434-e251a0b96877"

p = btle.Peripheral(address)
p.setDelegate(MyDelegate())

# p2 = btle.Peripheral(address)
# p2.setDelegate(MyDelegate())
# Setup to turn notifications on, e.g.
svc = p.getServiceByUUID(service_uuid)
# svc2 = p2.getServiceByUUID(service_uuid)
ch = svc.getCharacteristics(char_uuid)[0]
#ch_02 = svc.getCharacteristics(char2_uuid)[0]
"""
setup_data for bluepy noification-
"""
setup_data = b"\x01\x00"
ch.write(setup_data)
#ch_02.write(setup_data)
p.writeCharacteristic(ch.valHandle + 1, setup_data)
#p.writeCharacteristic(ch_02.valHandle + 1, setup_data)

# ch_data = p.readCharacteristic(ch.valHandle + 1)
# ch_data_02 = p2.readCharacteristic(ch_02.valHandle + 1)

"""print(type(ch_data))"""
# print(ch_data)

print("        ")
# print(ch_data_02) 

print("=== Main Loop ===")

while True:
    if p.waitForNotifications(1.0): # and p.waitForNotifications02(1.0):

                     
    # handleNotification() was called
          continue
      
    #    print("Waiting...")
    # Perhaps do something else here
