
# GUI Python3 example on Raspberry Pi to handle notification from
# ESP32 BLE_notify example.
# To install bluepy for Python3:
# $ sudo pip3 install bluepy

from bluepy import btle
import time
import os 

class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        # ... initialise here
    def handleNotification(self, cHandle, data):


		# ... perhaps check cHandle

		# # ... process 'data'  
        if(cHandle==0x002a):

            highbyte7=(data[1])
            lowbit7=(data[0])
            word7=(highbyte7<<8)|lowbit7
            print("the weight of J7  : " +str(word7))
            
            
  #-------------------------------------------------------------
        elif(cHandle==0x002d):


            highbyte=(data[0])
            lowbit=(data[1])
         #  print(data[0])
         # print(data[1])

            word=(highbyte<<8)|lowbit
            print("the weight of J5  : " +str(word))
            print("        ")
            time.sleep(1)
            os.system('clear')

## Initialisation  -------
#

# address = "08:3A:F2:6E:29:CA"
address = "A4:CF:12:6B:60:1E"
service_uuid = "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
char_uuid = "beb5483e-36e1-4688-b7f5-ea07361b26a8"
char_uuid_02 = "dd2ca829-8b7e-4a1a-936e-3409f2c85855"

p = btle.Peripheral(address)
p.setDelegate(MyDelegate())

 



# Setup to turn notifications on, e.g.
svc = p.getServiceByUUID(service_uuid)


ch = svc.getCharacteristics(char_uuid)[0]
ch_02 = svc.getCharacteristics(char_uuid_02)[0]
"""
setup_data for bluepy noification-
"""
setup_data = b"\x01\x00"
 #ch.write(setup_data)

p.writeCharacteristic(ch.valHandle + 1, setup_data)
p.writeCharacteristic(ch_02.valHandle + 1, setup_data)

ch_data = p.readCharacteristic(ch.valHandle + 1)
ch_data_02 = p.readCharacteristic(ch_02.valHandle + 1)

#print(type(ch_data))
#print(ch_data)



print("=== Connected to ESP32 of the Minibar-Livello ===")

while True:
    if p.waitForNotifications(1.0):
       
    # handleNotification() was called
        continue
    #    print("Waiting...")
    # Perhaps do something else here
