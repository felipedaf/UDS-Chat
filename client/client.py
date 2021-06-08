import socket
import sys

def send(sock, msg: str):
    message = msg.encode(encoding)
    msg_length = len(message)
    send_length = str(msg_length).encode(encoding)
    send_length += b" " * (64 - len(send_length))
    sock.send(send_length)
    sock.send(message)

def start(sock):
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


if __name__ == "__main__":
    sock = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_STREAM)
    SOCK_ADDR = "../temp/uds_socket"
    EXIT_MESSAGE = "!EXIT"
    encoding = "UTF-8"
    start(sock)

