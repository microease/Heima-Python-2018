#coding=utf-8
import socket
from multiprocessing import Process
import re
import sys
htmlRootDir = "/Users/huxiaoyi/Desktop/"
WSGIPYTHONPACH = "/Users/huxiaoyi/Desktop/wsgipy/"
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
    def startResponse(self,status,headers):
        responseHeaders = "HTPP/1.1" + status + "\r\n"
        
        for header in headers:
            responseHeaders += "%s:%s\r\n" %header
        self.responseHeaders = responseHeaders
        print(self.responseHeaders)
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
        
        if fileName.endswith(".py"):
            m = __import__(fileName[1:-3])
            env = {}
            responseBody = m.application(env,self.startResponse)
            response = self.responseHeaders + "\r\n" + responseBody
            print("此处有问题")
            print(response)
        else:
            if "/" == fileName:
                fileName = "index.html"
            try:
                file = open(htmlRootDir + fileName,"rb")
            except IOError: 
                responseStart = "HTTP/1.1 404 Not Found"
                responseHeaders = "Server:Huyankai Servers"
                responseBody = "This page is Not Found"
            else:
                fileData = file.read()
                file.close()
                responseStart = "HTTP/1.1 200 OK\r\n"
                responseHeaders = "Server:Huyankai Servers\r\n"
                responseBody = fileData.decode("utf-8")
            response = responseStart + responseHeaders + "\r\n" +responseBody
            print(response)
        clientSocket.send(bytes(response,"utf-8"))
        clientSocket.close()
def main():
    sys.path.insert(1,WSGIPYTHONPACH)
    httpServer = HTTPServers(8050)
    httpServer.start()
if __name__ == "__main__":
    main()