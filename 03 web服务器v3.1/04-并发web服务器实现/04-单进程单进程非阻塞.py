import socket

tcp_server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_tcp.bind(("", 7788))
tcp_server_tcp.listen(128)
tcp_server_tcp.setblocking(False)

client_socket_list = list()

while True:
    try:
        new_socket, new_addr = tcp_server_tcp.accept()
    except Exception as ret:
        print("没有新的客户端到来")
    else:
        print("只要没有产生异常，就意味着到来了一个新的客户端")
        new_socket.setblocking(False)
        client_socket_list.append(new_socket)

    for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv()
        except Exception as ret:
            print("这个客户端没有发送过来数据")
        else:
            if recv_data:
                print("客户端发送过来了数据")
            else:
                client_socket_list.remove(client_socket)
                client_socket.close()
