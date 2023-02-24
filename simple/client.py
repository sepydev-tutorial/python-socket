import socket

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.connect(('127.0.0.1', 12345))

full_message = ""
while True:
    msg = socket_obj.recv(8)
    if not msg:
        break
    full_message += msg.decode('utf-8')

print(full_message)
