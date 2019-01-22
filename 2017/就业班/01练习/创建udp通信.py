#coding=utf-8
from socket import *

#创建套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)

#绑定本地的相关信息
bindAddr = ('',7788)
udpSocket.bind(bindAddr)
#定义接收方地址
sendAddr = ('192.168.1.102',8082)

#从键盘获取数据
sendData = input("请输入您要发送的数据：")

print(sendData)
#发送数据到指定电脑
#此处是因为出现了一个错误，如果不加这行，python解释器会报错传的是str类型数据，所以必须把str类型数据转换成bytes类型数据
udpSocket.sendto(sendData.encode('utf-8'),sendAddr)

#关闭套接字
udpSocket.close()