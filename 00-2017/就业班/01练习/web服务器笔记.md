## 网络层级复习

应用层：解决要传递什么数据，怎么传，什么格式，传到哪里，应用层不管。应用层只管我要传递什么。

传输层：负责数据传输，UDP/TCP可以理解成普邮和挂号信，普通邮件邮局不管能不能送得到，挂号信则不一样，UDP传输没有返回确认，TCP相对比较稳定。

网络层：负责判断对方在哪里，在网络的哪个位置，例如IP协议，对方的IP地址就是你要传输的地址，IP地址唯一而且确定。目前普遍应用的还是IPV4,IPV6协议还没有完全应用起来。

链路层：链路层是具体的传输工具，应用层知道了数据，传输层传输数据，网络层判断对方在哪里，链路层则是物理上的工具。

## Socket编程复习

### 客户端和服务器端(C/S)

服务器端创建Socket套接字的方式：

TCP:ServerSocket = socket.socket(AF_INET,SOC_STREAM) 

UDP:ServerSocket = socket.socket(AF_INET,SOC_DGRAM) 

Socket.bind()

Socket.listen()

Socket.accept()

客户端创建Socket套接字的方式：

So = Socket.socket()

So.connect()

连接成功后：

TCP:So.send()/So.recv()

UDP:So.sendto()/So.recvFrom()

TCP和UDP的区别是，TCP传输需要对方确认，UDP传输数据过去就不管了。

### TCP三次握手和四次挥手

**三次握手**：

客户端：发送连接信息 seq=1

服务器端：发送响应 ack=2,seq=1

客户端：收到响应，回复给服务器响应 ack=2,seq=2

**四次挥手**：

客户端：发送close()信息，关闭客户到服务器的数据传输

服务器端：收到了close()信息，发回一个ACK

服务器端：关闭客户端的连接，发送一个FIN给客户端

客户端：发回ACK报文确认。

## HTTP和HTML

HTTP：超文本格式传输协议

HTML：超文本标记语言文件

**HTTP请求方式**：

GET：请求服务器数据

POST：修改数据

PUT：保存数据

DELETE：删除数据

OPTION：询问服务器的某种支持特性

HEAD：返回报文头数据