import socket


def main():
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("请输入服务器的IP：")
    server_port = input("请输入服务器的端口：")
    server_addr = (server_ip, server_port)
    tcp_client_socket.connect(server_addr)
    send_data = input("请输入要发送的数据：")
    tcp_client_socket.send(send_data.encode("utf-8"))
    tcp_client_socket.close()


if __name__ == '__main__':
    main()
