import socket


def send_msg(udp_socket):
    send_data = input("请输入你要发送的信息：")
    dest_ip = input("请输入对方的IP：")
    dest_port = input("请输入对方的端口号：")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data.decode("utf-8")))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定信息
    udp_socket.bind(("", 7788))
    while True:
        # 发送数据
        send_msg(udp_socket)
        # 接收数据并显示
        recv_msg(udp_socket)


if __name__ == '__main__':
    main()
