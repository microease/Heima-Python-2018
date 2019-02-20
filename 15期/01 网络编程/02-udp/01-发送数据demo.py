import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest_ip = input("请输入对方的ip地址：")
    dest_port = input("请输入对方的端口号：")
    send_data = input("请输入要发送的数据：")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip,dest_port))
    udp_socket.close()


if __name__ == '__main__':
    main()
