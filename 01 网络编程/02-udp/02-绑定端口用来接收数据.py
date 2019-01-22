import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localaddr = ("", 7788)
    udp_socket.bind(localaddr)
    udp_socket.close()
    recv_data = udp_socket.recvfrom(1024)
    recv_msg = recv_data[0]
    send_addr = recv_data[1]

    # print(recv_data[0])
    print("%s:%s" % (str(send_addr), recv_msg.decode("utf-8")))

    if __name__ == '__main__':
        main()
