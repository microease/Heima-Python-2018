import socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.listen(128)
    while True:
        new_client_socket, client_addr = tcp_server_socket.accept()
        print(client_addr)
        while True:
            recv_data = new_client_socket.recv(1024)
            print(recv_data)
            if recv_data:
                new_client_socket.send("haha".encode("utf-8"))
            else:
                break
        new_client_socket.close()


if __name__ == '__main__':
    main()
