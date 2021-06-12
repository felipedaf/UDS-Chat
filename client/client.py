import socket
import sys
from messages import format

encoding = "UTF-8"

def send(sock, msg: str):
    messages = format.craete_message(msg, encoding)
    sock.send(messages[0])
    sock.send(messages[1])

def start():
    sock = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_STREAM)
    SOCK_ADDR = "temp/uds_socket"
    EXIT_MESSAGE = "!EXIT"
    try:
        sock.connect(SOCK_ADDR)
    except socket.error:
        print(f"Some error occured!")
        sys.exit(1)

    try:
        while True:
            msg = input("type a message: ")
            send(sock, msg)
            if msg == EXIT_MESSAGE:
                break
    except KeyboardInterrupt:
        send(sock, EXIT_MESSAGE)
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
