import socket

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.bind(('127.0.0.1', 12345))
socket_obj.listen(5)

while True:
    client_socket, address = socket_obj.accept()
    print(f"Connection from {address} has been established!")
    client_socket.send(bytes("Welcome to the Mohammad server!", "utf-8"))
    client_socket.close()


