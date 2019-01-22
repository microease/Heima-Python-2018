import socket
import re
import select

def servive_client(new_socket, request):
    request_lines = request.splitlines()
    print("")
    print(">" * 20)
    print(request_lines)

    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name =="/":
            file_name = "/index.html"

    try:
        f = open("./html" +file_name,"rb")
