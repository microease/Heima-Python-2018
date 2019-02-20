import socket


def server_client(new_socket):
    request = new_socket.recv(1024)
    print(request)
    response = "HTTP/1.1 200 OK \r\n"
    response += "\r\n"
    response += "hahah"
    new_socket.send(response.encode("utf-8"))
    new_socket.close()


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定
    tcp_server_socket.bind(("", 2333))
    # 变为监听套接字
    tcp_server_socket.listen(128)
    # 等待新的客户端连接
    new_socket, client_addr = tcp_server_socket.accept()
    # 为这个客户端服务
    server_client(new_socket)


if __name__ == '__main__':
    main()
