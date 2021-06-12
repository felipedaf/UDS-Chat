def craete_message(msg, encoding):
    message = msg.encode(encoding)
    msg_length = len(message)
    send_length = str(msg_length).encode(encoding)
    send_length += b" " * (64 - len(send_length))
    return (send_length, message)