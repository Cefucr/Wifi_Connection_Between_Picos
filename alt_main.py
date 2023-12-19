from machine import Pin,ADC
import network
import time
import socket

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('surffi', '')
while not wlan.isconnected() and wlan.status() >= 0:
    print("Waiting to connect:")
    time.sleep(1)
    
wlan.status()
wlan.ifconfig()

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
cl, addr = s.accept()
print("IP = " + str(wlan.ifconfig()[0]))
print("Connected!\n")
inpu = input("Receive or send[R/S]: ")

def receivevalue():
    print("Receiving...")
    cl.send(b"GET Data") # Send request
    ss=str(cl.recv(512)) # Store reply
    time.sleep(0.2)
    return ss

def sendvalue(val):
    print("Sending...")
    #request = cl.recv(1024)
    cl.send(str(val))
    print("Sent " + str(val))
    
if inpu == "R":
    value = str(receivevalue())
    print("Got " + value[1:])
elif inpu == "S":
    sendvalue("value") 
else:
    print("Invalid input. Please try again.")
