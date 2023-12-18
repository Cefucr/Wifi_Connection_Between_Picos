from machine import Pin,ADC
import network
import time
import socket

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('ssid', 'pin')
while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)
wlan.status()
wlan.ifconfig()
print("IP = " + str(wlan.ifconfig()[0]))
inpu = input("Receive or send[R/S]: ")

def receivevalue():
    print("Receiving...")
    ai = socket.getaddrinfo("ip", 80) #The other devices ip address
    addr = ai[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(b"GET Data")
    ss=str(s.recv(512))
    s.close()
    time.sleep(0.2)
    
    return ss

def sendvalue(val):
    print("Sending...")
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)
    try:
        cl, addr = s.accept()
        request = cl.recv(1024)
        cl.send(str(val))
        print("Sent " + str(val))
        cl.close()
    except OSError as e:
        cl.close
        print("Error Connection Terminated")
        
if inpu == "R":
    received = str(receivevalue())
    print("Got " + received[1:])
elif inpu == "S":
    while True:
        sendvalue("value")
else:
    print("Invalid input. Please try again.")
