import network

def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print ("connecting to network")
        wlan.connect("valorant","17031986")
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
      
do_connect()
