import cv2
import paho.mqtt.client as mqtt
import time

from cvzone.HandTrackingModule import HandDetector
detector=HandDetector(detectionCon=0.5,maxHands=2)

cap=cv2.VideoCapture(0)
count=0
def one():
    mqttBroker ="192.168.0.23"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("test2",(bytes("one",'utf-8')))     



def two():
    mqttBroker ="192.168.0.23"
    client = mqtt.Client("raspberry pi 401")
    client.connect(mqttBroker)
    client.publish("test2",(bytes("two",'utf-8')))     

def three():
    mqttBroker ="192.168.0.23"
    client = mqtt.Client("raspberry pi 401")
    client.connect(mqttBroker)
    client.publish("test2",(bytes("three",'utf-8')))    
    

def goodbye():
    mqttBroker ="192.168.0.23"
    client = mqtt.Client("raspberry pi 40")
    client.connect(mqttBroker)
    client.publish("test2",(bytes("goodbye",'utf-8')))     

  
    

while True:
    ret,frame=cap.read()
    count += 1
    if count % 14 != 0:
        continue
    frame=cv2.flip(frame,-1)
    hands,frame=detector.findHands(frame)
    if not hands:
        goodbye()
    else: 
        hands1=hands[0]
        bbox=hands1["bbox"]
        x,y,w,h=bbox
        fingers1=detector.fingersUp(hands1)
        count = fingers1.count(1)
        print('Count of 1:', count)
        if count==1:
            one()
        elif count==2:
             two()
        elif count==3:
            three()
        elif count==5:
            goodbye()
         

        
   
           
   
        
    frame=cv2.imshow("FRAME",frame)
   
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()
