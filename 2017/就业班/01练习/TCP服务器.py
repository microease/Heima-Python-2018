from socket import *
severSocket = socket(AF_INET,SOCK_STREAM)
#创建套接字
severSocket.bind(("",8899))
#绑定IP
severSocket.listen(5)
#最多监听5个端口
clientSocket,clientInfo = severSocket.accept()
#clientSocket表示新的客户端
#clientInfo表示新的客户端的ip和端口信息
recvData = clientSocket.recv(1024)
#将接受到的数据用recvData保存
print("%s:%s"%(str(clientInfo),recvData))
#打印接收到的数据
clientSocket.close()
severSocket.close()