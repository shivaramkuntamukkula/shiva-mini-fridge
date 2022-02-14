
# GUI Python3 example on Raspberry Pi to handle notification from
# ESP32 BLE_notify example.
# To install bluepy for Python3:
# $ sudo pip3 install bluepy

from bluepy import btle
import time
import os 

xx=""
enbs=0
class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)
        # ... initialise here
     

  
    def writeCharacteristic(handle,val,withResponse):
        print(withResponse)



    def handleNotification(self, cHandle, data):

        print("this reached here")


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
            p = btle.Peripheral(address)
            p.setDelegate(MyDelegate())
            enb=0
            print("Connected to ESP32 of the Minibar-Livello "+str(enb))
        except:
            print("not connected")  
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
            g= bytes('start', 'utf-8')
            p.writeCharacteristic(handle, g)
            #if p.waitForNotifications(1.0):
            print("inside the try with CVS   "+ str(enb))
            #    continue
            enbs=3
            enb=2
        except:
            print("something went wrong~!")
            enb=1

 #   print("loop started ")
   #= bytes('start', 'utf-8')
 #   p.writeCharacteristic(handle, g)
    #writeCharacteristic(handle, val, withResponse=True)
    if enbs==3 and enb==2:
        print("waiting for notification"+str(enb))
        if p.waitForNotifications(1.0):
            
            continue
    
 #   if p.waitForNotifications(1.0):
       

    # handleNotification() was called
  #      continue
    #    print("Waiting...")
    # Perhaps do something else here
