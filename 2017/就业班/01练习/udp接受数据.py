from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)
#绑定端口
udpSocket.bind(('',8082))
#接收传过来的内容
recvData = udpSocket.recvfrom(1024)
#解包，传过来的数据格式为内容,ip和端口
content,dataInfo = recvData
#打印内容
print("内容是：%s"%content.decode("utf-8"))