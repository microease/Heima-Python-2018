#coding=utf-8
from socket import *
tcpClientSocket = socket(AF_INET,SOCK_STREAM)
serverAddr = ("192.168.1.102",8080)
tcpClientSocket.connect(serverAddr)
tcpClientSocket.send("我是胡炎凯".encode("gb2312"))
recvData = tcpClientSocket.recv(1024)
print("recvData:%s"%recvData)
tcpClientSocket.close()