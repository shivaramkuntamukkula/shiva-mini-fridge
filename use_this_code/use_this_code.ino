/*
    Video: https://www.youtube.com/watch?v=oCMOYS71NIU
    Based on Neil Kolban example for IDF: https://github.com/nkolban/esp32-snippets/blob/master/cpp_utils/tests/BLE%20Tests/SampleNotify.cpp
    Ported to Arduino ESP32 by Evandro Copercini
    updated by chegewara

   Create a BLE server that, once we receive a connection, will send periodic notifications.
   The service advertises itself as: 4fafc201-1fb5-459e-8fcc-c5c9c331914b
   And has a characteristic of: beb5483e-36e1-4688-b7f5-ea07361b26a8

   The design of creating the BLE server is:
   1. Create a BLE Server
   2. Create a BLE Service
   3. Create a BLE Characteristic on the Service
   4. Create a BLE Descriptor on the characteristic
   5. Start the service.
   6. Start advertising.

   A connect hander associated with the server starts a background task that performs notification
   every couple of seconds.
*/
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>
#include "HX711.h"
const int LOADCELL_DOUT_PIN_J7 = 15;
const int LOADCELL_DOUT_PIN_J5 = 04;
const int LOADCELL_SCK_PIN = 2;
uint32_t J5;
uint32_t J7;
HX711 scale_J7;
HX711 scale_J5;

BLEServer* pServer = NULL;
BLECharacteristic* pCharacteristic = NULL;
BLECharacteristic *pCharacteristic_02;
bool deviceConnected = false;
bool oldDeviceConnected = false;
uint8_t value;

// See the following for generating UUIDs:
// https://www.uuidgenerator.net/

#define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"
#define CHARACTERISTIC_UUID_02 "dd2ca829-8b7e-4a1a-936e-3409f2c85855"

class MyServerCallbacks: public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) {
      deviceConnected = true;
    };

    void onDisconnect(BLEServer* pServer) {
      deviceConnected = false;
    }
};



void setup() {
 
  Serial.begin(115200);
scale_J7.begin(LOADCELL_DOUT_PIN_J7, LOADCELL_SCK_PIN);
  scale_J5.begin(LOADCELL_DOUT_PIN_J5, LOADCELL_SCK_PIN);

  // Create the BLE Device
  BLEDevice::init("ESP32");

  // Create the BLE Server
  pServer = BLEDevice::createServer();
  pServer->setCallbacks(new MyServerCallbacks());

  // Create the BLE Service
  BLEService *pService = pServer->createService(SERVICE_UUID);

  // Create a BLE Characteristic
  pCharacteristic = pService->createCharacteristic(
                      CHARACTERISTIC_UUID,
                      BLECharacteristic::PROPERTY_READ   |
                      BLECharacteristic::PROPERTY_NOTIFY 
                       );

  pCharacteristic_02 = pService->createCharacteristic(
                                         CHARACTERISTIC_UUID_02,
                                         BLECharacteristic::PROPERTY_READ   |
                                         BLECharacteristic::PROPERTY_NOTIFY
                                       );


  // https://www.bluetooth.com/specifications/gatt/viewer?attributeXmlFile=org.bluetooth.descriptor.gatt.client_characteristic_configuration.xml
  // Create a BLE Descriptor
  pCharacteristic->addDescriptor(new BLE2902());
  pCharacteristic_02->addDescriptor(new BLE2902());

  // Start the service
  pService->start();

  // Start advertising
  BLEAdvertising *pAdvertising = BLEDevice::getAdvertising();
  pAdvertising->addServiceUUID(SERVICE_UUID);
  pAdvertising->setScanResponse(false);
  pAdvertising->setMinPreferred(0x0);  // set value to 0x00 to not advertise this parameter
  BLEDevice::startAdvertising();
  Serial.println("Waiting a client connection to notify...");
}
/*
byte *converter(long n){
  byte buf[4];
  
buf[0] = (byte) n;
buf[1] = (byte) n >> 8;
buf[2] = (byte) n >> 16;
buf[3] = (byte) n >> 24;
 return buf;
  }*/

void loop() {
  long reading_J7 = scale_J7.read();
    long reading_J5 = scale_J5.read();
uint32_t value = 0;
   

/*
for(int i = 0; i < 4; i++){
     readings[i] = readings % 10;  // remainder of division with 10 gets the last digit
     readings /= 10;     // dividing by ten chops off the last digit.
}*/
    delay(200);
    int readings[2];
    int message = Serial.read();
    Serial.print(message);
    if (message == 49){
      Serial.print(message);
      int i;
       for( i=1;i<1000;i++){
        long int tmpval= (7806502-reading_J7)/i;
          if(abs(tmpval-500)<=4){
              Serial.println("J7 calibration value="+String(i));
              delay(200);
            }
        }
        for(i=1;i<1000;i++){
          long int tmpval2=(5070819-reading_J5)/i;
          if(abs(tmpval2-200)<=1){
              Serial.println("J5 calibration value="+String(i));
            }
        }
     }
     else{
        J5={(abs((reading_J5-5341487))/565)};
        
        //Serial.print(a);
        J7={(abs((7806450-reading_J7))/131)};
        
       // Serial.println("Value of the first (J7) scale :"+String(readings[0]));
        
        
    //    Serial.println("Value of the second (J5) scale :" + String(readings[1]));

Serial.print("J5 : ");Serial.println(J5);
Serial.print("J7 :");Serial.println(J7);
//Serial.print("Offset Val of  J7 :");Serial.println(J7);
//Serial.print("Offset Val of  J5 :");Serial.println(reading_J5); 

         }

    delay(100);

  
    // notify changed value
    if (deviceConnected) {

        
          
        byte lowByte = ((J5 >> 0) & 0xFF);
     // Now shift the binary number 8 bits to the right  
        byte highByte = ((J5 >> 8) & 0xFF);
        pCharacteristic->setValue((uint8_t*)&highByte ,2);
        pCharacteristic->setValue((uint8_t*)&lowByte , 2);
        pCharacteristic->notify();
        delay(400);
        
        
        highByte = ((J7 >> 0) & 0xFF);
        lowByte = ((J7 >> 8) & 0xFF);
         //Serial.print("sending 2");pCharacteristic_02->setValue((uint8_t*)&highByte , 2);
          pCharacteristic_02->setValue((uint8_t*)&lowByte , 2);
          pCharacteristic_02->notify();

          
         
        delay(400); // bluetooth stack will go into congestion, if too many packets are sent, in 6 hours test i was able to go as low as 3ms
    }
    // disconnecting
    if (!deviceConnected && oldDeviceConnected) {
        delay(500); // give the bluetooth stack the chance to get things ready
        pServer->startAdvertising(); // restart advertising
        Serial.println("start advertising");
        oldDeviceConnected = deviceConnected;
    }
    // connecting
    if (deviceConnected && !oldDeviceConnected) {
        // do stuff here on connecting
        oldDeviceConnected = deviceConnected;
    }
}
