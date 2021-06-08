import json
import message
import re
EXIT_MESSAGE = "!EXIT"
FORMAT = "UTF-8"

def start_communication(conn, chat_handler, user_handler, id):
    print(f"[{id}] Successfully connected!")

    while True:
        msg_length = conn.recv(64).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == EXIT_MESSAGE:
            break

        message_checker(conn, msg, chat_handler, user_handler, id)

        print(f"[{id}]: {msg}")


def message_checker(conn, msg, ch, uh, id):
    prefixes = [
        r"\$USER_DISCONNECTION\$!",
        r"\$USER_MESSAGE\$!",
        r"\$USER_AUTHENTICATION\$!"
    ]

    matched_prefix = None

    for k in prefixes:
        prefix = f"^{k}"
        matched_prefix = re.match(prefix, msg)
        if matched_prefix:
            break

    if not matched_prefix:
        return

    message_content = json.loads(msg[len(matched_prefix[0]):])

    if matched_prefix[0] == "$USER_AUTHENTICATION$!":
        user_auth(conn, uh, id, message_content)
    elif matched_prefix[0] == "$USER_MESSAGE$!":
        user_message(ch, id, message_content)
    elif matched_prefix[0] == "$DISCONNECTION$!":
        disconnection(uh, id)


def user_auth(conn, uh, id, content):
    try:
        uh.add_user(id, content["username"], conn)
    except KeyError:
        print("Disallowed message content")

    # Send a message to all users, saying that a new user has connected.


def user_message(ch, id, content):
    user_message = content["message"]
    receiver = int(content["receiver"])
    new_message = message.Message(id, user_message)

    ch.start_chat(id, receiver)
    ch.send_message(id, receiver, new_message)

    # Send a message to receiver client with the sender's message.

def disconnection(uh, id):
    uh.delete_user(id)

    # Send a message to all users warning that this user is disconnected
