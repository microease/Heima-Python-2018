#coding=utf-8
import socket
from multiprocessing import Process
import re
htmlRootDir = "/Users/huxiaoyi/Desktop/"
class HTTPServers(object):
    def __init__(self,port):
        self.serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1 )
        self.serverSocket.bind(("",port))
        
    def start(self):
        self.serverSocket.listen(128)
        while True:
            clientSocket,clientAddress = self.serverSocket.accept()
            hadleClientProcess = Process(target=self.handleClient,args=(clientSocket,))
            hadleClientProcess.start()
            clientSocket.close()
        
    def handleClient(self,clientSocket):
        requestData = clientSocket.recv(1024)
        print (requestData)

        requestDataLines = requestData.splitlines()
        for line in requestDataLines:
            print(line)
        requestStartline = requestDataLines[0]
        print (requestStartline)
        #提取用户请求的文件名
        fileName = re.match(r"\w+ +(/[^ ]*) ",requestStartline.decode("utf-8")).group(1)
        
        if "/" == fileName:
            fileName = "index.html"
        try:
            file = open(htmlRootDir + fileName,"rb")
        except IOError: 
            responseStart = "HTTP/1.1 404 Not Found"
            responseheaders = "Server:Huyankai Servers"
            responseBody = "This page is Not Found"
        else:
            fileData = file.read()
            file.close()
            responseStart = "HTTP/1.1 200 OK\r\n"
            responseheaders = "Server:Huyankai Servers\r\n"
            responseBody = fileData.decode("utf-8")
        response = responseStart + responseheaders + "\r\n" +responseBody
        print(response)
        clientSocket.send(bytes(response,"utf-8"))
        clientSocket.close()
def main():
    httpServer = HTTPServers(8025)
    httpServer.start()
if __name__ == "__main__":
    main()