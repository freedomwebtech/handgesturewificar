
from umqtt.simple import MQTTClient
import machine
from time import sleep


server="192.168.0.23"
c = MQTTClient("umqtt_client", server)

p = machine.PWM(machine.Pin(5), freq=10000)
p1 = machine.PWM(machine.Pin(4), freq=10000)
p2 = machine.PWM(machine.Pin(12), freq=10000)
p3 = machine.PWM(machine.Pin(13), freq=10000)
led = machine.Pin(16, machine.Pin.OUT)


def msg(a,b):
    data=(str(b,'utf-8'))
    print(data)
    if "one" in data:
        for i in range(600):
            p.duty(0)
            p1.duty(i)
            p2.duty(i)
            p3.duty(0)
    if "two" in data:
        for j in range(600):
            p.duty(j)
            p1.duty(0)
            p2.duty(0)
            p3.duty(j)
    if "three" in data:
        for j in range(900):
            p.duty(0)
            p1.duty(j)
            p2.duty(0)
            p3.duty(j)
           
   
    if "goodbye" in data:
            p.duty(0)
            p1.duty(0)
            p2.duty(0)
            p3.duty(0)
        
                    
    
   
                    
            
    
    
    
def client():
   
    c.set_callback(msg)
    c.connect()
    c.subscribe("test2")
    c.wait_msg()
    c.check_msg()
    c.disconnect()
while True:
     led.value(0)
     sleep(0.5)
     led.value(1)
     sleep(0.5)
     client()
