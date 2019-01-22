from socket import *
#导入模块
serverSocket = socket(AF_INET,SOCK_STREAM)
#创建套接字
#serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

localAddr = ('',7788)
serverSocket.bind(localAddr)
#绑定本地端口
serverSocket.listen(10)
#将socket变成监听套接字
serverSocket.setblocking(False)
#让这个socket变成非堵塞
clientAddrList = []
#保存已经链接的客户端
while True:
	#等待新的客户端的到来
	try:
		clientSocket,clientAddr = serverSocket.accept()
	except:
		pass
	else:
		print("一个新的客户端到来：%s"%str(clientAddr))
		clientSocket.setblocking(False)
		clientAddrList.append((clientSocket,clientAddr))
		print(clientAddrList)
	#打印客户端发送的数据
	for clientSocket,clientAddr in clientAddrList:
		try:
			recvData = clientSocket.recv(1024)
		except:
			pass
		else:
			if len(recvData)>0:
				print("%s:%s"%(str(clientAddr),recvData))
			else:
				clientSocket.close()
				clientAddrList.remove((clientSocket,clientAddr))
				print("%s已经下线"%str(clientAddr))