#coding=utf-8
from threading import Thread
from socket import *
#收数据，然后打印
def recvData():
	while True:
		recvInfo = udpSocket.recvfrom(1024)
		print("\r>>%s:%s"%(str(recvInfo[1]),recvInfo[0].decode("gb2312")))
#检测键盘，发数据
def sendData():
	while True:
		sendInfo = input("<<")
		udpSocket.sendto(sendInfo.encode("gb2312"),(destIP,destPort))
udpSocket = None
destIP = ""
destPort = 0
def main():
	global udpSocket
	global destIP
	global destPort
	destIP = input("对方的IP：")
	destPort = int(input("对方的端口："))
	udpSocket = socket(AF_INET,SOCK_DGRAM)
	udpSocket.bind(("",8093))

	tr = Thread(target=recvData)
	ts = Thread(target=sendData)

	tr.start()
	ts.start()

	tr.join()
	ts.join()

if __name__ == "__main__":
	main()