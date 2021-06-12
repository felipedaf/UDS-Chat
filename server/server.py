import os
import sys
import threading
import socket
from .chat_handler import ChatHandler
from .user_handler import UserHandler
from .communication_handler import start_communication

increment_id = 0

def listen_communication(conn, ch, uh, id):
    start_communication(conn, ch, uh, id)
    print(f"Client {id} was disconnected!")
    conn.close()

def start():
    global increment_id
    c_handler = ChatHandler()
    u_handler = UserHandler()

    SOCK_ADDR = "temp/uds_socket"

    try:
        os.unlink(SOCK_ADDR)
    except OSError:
        if os.path.exists(SOCK_ADDR):
            raise

    sock = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_STREAM)
    sock.bind(SOCK_ADDR)
    sock.listen()

    try:
        while True:
            conn, addr = sock.accept()
            increment_id += 1
            thread = threading.Thread(
                target=listen_communication,
                args=(conn, c_handler, u_handler, increment_id)
            )

            thread.start()
    except KeyboardInterrupt:
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        sys.exit(0)
