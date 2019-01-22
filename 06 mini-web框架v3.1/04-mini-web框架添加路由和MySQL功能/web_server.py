import socket
import re
import multiprocessing
import time
import sys


class WSGIServer(object):
    def __init__(self, port, app, static_path):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_server_socket.bind(("", port))
        self.tcp_server_socket.listen(128)
        self.application = app
        self.static_path = static_path

    def server_client(self, new_socket):
        request = new_socket.recv(1024).decode("UTF-8")
        request_lines = request.splitlines()
        print(">" * 20)
        print(request_lines)
        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*),request_lines[0]")
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"
        if not file_name.endswith(".py"):
            try:
                f = open(self.static_path + file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "---file not found"
                new_socket.send(response.encode("utf-8"))
            else:
                html_content = f.read()
                f.close()
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                new_socket.send(response.encode("utf-8"))
                new_socket.send(html_content)
        else:

