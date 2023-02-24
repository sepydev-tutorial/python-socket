import socket
import select
import errno
import sys
from contextlib import suppress

HEADER_LENGTH = 10

user_name = input("User name :")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 1234))
client_socket.setblocking(False)

user_name_enc = user_name.encode('utf-8')
user_header = f"{len(user_name_enc):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(user_header + user_name_enc)

while True:
    message = input(f"{user_name}>")
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        while True:
            #     receive other messages
            receive_user_header = client_socket.recv(HEADER_LENGTH)
            if not receive_user_header:
                print("connection closed by server")
                sys.exit()

            read_length = int(receive_user_header.decode('utf-8'))
            user = client_socket.recv(read_length).decode('utf-8')

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8'))
            message = client_socket.recv(message_length).decode('utf-8')
            print(f"{user}>{message}")
    except IOError as err:
        if err.errno not in [errno.EAGAIN, errno.EWOULDBLOCK]:
            print('Reading error', str(err))
            sys.exit()
        continue
    except Exception as ex:
        print(str(ex))
        sys.exit()
