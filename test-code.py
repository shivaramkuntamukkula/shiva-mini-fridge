	# Python3 example on Raspberry Pi to handle notification from
# ESP32 BLE_notify example.
# To install bluepy for Python3:
# $ sudo pip3 install bluepy

from bluepy import btle
import matplotlib.pyplot as plt
import time
from os import system

from tkinter import *

window = Tk()
window.geometry('600x600')

window.title("Weights of the minibar")

window.mainloop()



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
        #print(type(data))
        #print(dir(data))
       # print(data)
        print("The weight readings are :  "+   str(int(data[0])) + " grams\n" )
        time.sleep(0.6)
        
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
#char_uuid_02 = "beb5483e-36e1-4688-b7f5-ea07361b26a9"

p = btle.Peripheral(address)
p.setDelegate(MyDelegate())

# Setup to turn notifications on, e.g.
svc = p.getServiceByUUID(service_uuid)
ch = svc.getCharacteristics(char_uuid)[0]
#ch_02 = svc.getCharacteristics(char_uuid_02)[0]
"""
setup_data for bluepy noification-
"""
setup_data = b"\x01\x00"
#ch.write(setup_data)
p.writeCharacteristic(ch.valHandle + 1, setup_data)
#p.writeCharacteristic(ch_02.valHandle + 1, setup_data)

ch_data = p.readCharacteristic(ch.valHandle + 1)
#ch_data_02 = p.readCharacteristic(ch_02.valHandle + 1)

"""print(type(ch_data))"""
print(ch_data)
print("hellllloooooooooooooooooooooooo")
print("        ")
#print(ch_data_02)

print("=== Main Loop ===")

while True:
    if p.waitForNotifications(1.0):
                     
# handleNotification() was called
          continue
      
    #    print("Waiting...")
    # Perhaps do something else here
