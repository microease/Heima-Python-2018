import socket
import multiprocessing


def server_client(new_socket):
    request = new_socket.recv(1024).decode("utf-8")
    print(request)
    response = "HTTP/1.1 200 OK \r\n"
    response += "\r\n"
    # response += "hahah"
    f = open("./html/index.html", "rb")
    html_content = f.read()
    f.close()
    new_socket.send(response.encode("utf-8"))
    new_socket.send(html_content)
    new_socket.close()


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定
    tcp_server_socket.bind(("", 2333))
    # 变为监听套接字
    tcp_server_socket.listen(128)
    while True:
        # 等待新的客户端连接
        new_socket, client_addr = tcp_server_socket.accept()
        p = multiprocessing.Process(target=server_client, args=(new_socket,))
        p.start()
        new_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
