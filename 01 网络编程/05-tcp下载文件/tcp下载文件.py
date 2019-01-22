import socket

def main():
	#创建套接字
	tcp_socket = socket.socket(socket.AF_INET,socket_STREAM)
	# 获取服务器的端口和IP
	dest_ip = input("请输入服务器的IP:")
	dest_port = input("请输入服务器的端口号：")
	tcp_socket.connect((dest_ip,dest_ports))
	#获取要下载的文件名称
	download_file_name = input("请输入要下载的文件名称：")
	tcp_socket.send(download_file_name.encode("utf-8"))
	recv_data = tcp_socket.recv(1024*1024)
	with open("[新]"+download_file_name，"wb") as f:
		f.write(recv_data)
	tcp_socket.close()
	

if __name__ == '__main__':
	main()