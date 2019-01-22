import struct
from socket import *

sendData = struct.pack("!H8sb5sb",1,"test.jpg",0,"octet",0)
udpSocket = socket(AF_INET,SOCK_DGRAM)
udpSocket.sendto(sendData.encode("utf-8"),("192.168.1.102",69))
udpSocket.close() 
result = struct.unpack("!HH",recvData[:4])
print(result)