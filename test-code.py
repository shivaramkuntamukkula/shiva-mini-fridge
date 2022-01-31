# Python3 example on Raspberry Pi to handle notification from
# ESP32 BLE_notify example.
# To install bluepy for Python3:
# $ sudo pip3 install bluepy

from bluepy import btle
import matplotlib.pyplot as plt
import time
from os import system
import tkinter as tk
from tkinter import *
#from PIL import ImageTk,Image
window = Tk()

window.title("Minibar")

window.geometry('400x400')

lbl = Label(window, text="Click  to connect to the ESP32 board via BLE       ")
say = Label(window)
lbl.grid(column=50, row=20)
say.grid(column=100, row=100)

condition=True 
 

def infinite_loop(): 
   if condition: 
      # lbl.configure(text=str(data[0]))

        

       p.waitForNotifications(1.0)
       
   # Call the infinite_loop() again after 1 sec 
  
       window.after(500, infinite_loop) 
   
      
def start():
          condition=True 
          say.configure(text="  connecting to Esp32 board BLE " )
          time.sleep(7) 
      
def stop():
       
          condition=False 
          window.destroy()

#def clicked():
lbl.configure(text="Connecting to ESP32 BLE")
time.sleep(4)
   #    window.destroy()

btn1 = Button(window, text="start ", command=start)
btn1.place(x=100, y=50)
#btn.grid(column=3, row=3)

btn = Button(window, text="Disconnect ESP32 ", command=stop)
btn.place(x=100, y=150)
#btn.grid(column=100, row=100)

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

        lbl.configure(text="  The reading is  :   " + str(data[0]) + "  Grams",font=("Helvetica",18),bd=3,relief="sunken")
  
        label=Label(window,text="hi",font=("Helvetica",18),bd=1,relief="sunken",justify="right")
     #   label.pack(pady=20,ipady=10,ipadx=10)
        print("The weight readings are :  "+   str(data[0]) + " grams\n" )
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

#print(ch-data

print("connecting to ESP32")
print("        ")
#print(ch_data_02)

print("Connected.... Receiving Data Via BLE")
print("                                     ")
#while True:
     


         #if p.waitForNotifications(1.0):
#window.mainloop()
                #print("hi")
#    if p.waitForNotifications(1.0):
                     
# handleNotification() was called
               # continue
      
    #    print("Waiting...")
    # Perhaps do something else here
window.after(500, infinite_loop) 
         
window.mainloop()
