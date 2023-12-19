import socket

#For server side
#s = socket.socket()
#s.bind(("0.0.0.0", 80))
#s.listen()
#(cl, addr) = s.accept()

#For client side
#cl = socket.socket()
#cl.connect((ip,'port'))


def senddata(data):
    cl.send(data)

def receivedata():
    return cl.recv(1024)


inp = input("What do? Send or Receive(S/R): ")

if(inp == "S"):
    senddata("lahetetty")
elif(inp == "R"):
    print("Got: " + str(receivedata()))
else:
    print("Dumbass")
